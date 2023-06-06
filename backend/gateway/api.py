
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncpg
from redis import asyncio as aioredis
import httpx
import os

app = FastAPI()
# enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Change this to the frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

host = os.environ.get("POSTGRES_HOST", "localhost")
user = os.environ.get("POSTGRES_USER", "karelia")
password = os.environ.get("POSTGRES_PASSWORD", "postgres")
database = os.environ.get("POSTGRES_DB", "iot_devices")

# Pydantic model
class Datapoint(BaseModel):
    object_id: str
    jsonpath: str
    topic: str
    entity_id: Optional[str] = Field(None, min_length=1, max_length=255)
    entity_type: Optional[str] = Field(None, min_length=1, max_length=255)
    attribute_name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = ''
    matchDatapoint: Optional[bool] = False
  
class DatapointUpdate(BaseModel):
    entity_id: Optional[str] = Field(None, min_length=1, max_length=255)
    entity_type: Optional[str] = Field(None, min_length=1, max_length=255)
    attribute_name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = ''
    
# Database connection settings
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"
ORION_URL = os.environ.get("ORION_URL", "http://localhost:1026")
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

@app.on_event("startup")
async def startup():
    """
    Create a pool of connections to the database. The pool size is 10 connections.
    What it is supposed to achieve is that the gateway can handle 10 concurrent requests (is this appropriate for our use case?)
    """
    app.state.pool = await asyncpg.create_pool(DATABASE_URL)
    app.state.redis = await aioredis.from_url(REDIS_URL)
    
@app.on_event("shutdown")
async def shutdown():
    """
    Close the pool of connections to the database. This is to prevent the pool from being left open when the gateway is shut down.
    """
    await app.state.pool.close()
    
async def get_connection():
    """
    Get a connection from the pool of connections to the database. This is to ensure that the gateway does not have to create a new connection
    to the database for every request. Instead, it can reuse an existing connection from the pool for efficiency.
    """
    async with app.state.pool.acquire() as connection:
        # async with is used to ensure that the connection is released back to the pool after the request is done
        # a yield statement is used to return the connection to the caller
        yield connection
        
async def postgres_notify(channel: str, payload: str, conn: asyncpg.Connection):
    """
    Send a notification to the database. This is to notify the database that a new datapoint has been added to the gateway.
    """
    print(f"Sending notification to channel {channel} with payload {payload}")
    await conn.execute(f"NOTIFY {channel}, '{payload}'")

@app.get("/data", response_model=List[Datapoint],
            summary="Get all datapoints from the gateway",
            description="Get all datapoints from the gateway. This is to allow the frontend to display all the registered datapoints in the database.")
async def get_datapoints(conn: asyncpg.Connection = Depends(get_connection)):
    rows = await conn.fetch("SELECT object_id, jsonpath, topic, entity_id, entity_type, attribute_name, description FROM datapoints")
    return rows

@app.get("/data/{object_id}", response_model=Datapoint,
            summary="Get a specific datapoint from the gateway",
            description="Get a specific datapoint from the gateway. This is to allow the frontend to display a specific datapoint in the database. \
                        If the datapoint is not found, an error will be raised.")
async def get_datapoint(object_id: str, conn: asyncpg.Connection = Depends(get_connection)):
    row = await conn.fetchrow(
        """SELECT * FROM datapoints WHERE object_id=$1""",
        object_id
    )
    if row is None:
        raise HTTPException(status_code=404, detail="Device not found!")
    return row

@app.post("/data", response_model=Datapoint, status_code=201,
          summary="Add a new datapoint to the gateway",
          description="Add a new datapoint to the gateway. This is to allow to add new datapoints to the gateway. \
                       In (a very unlikely) case where the datapoint was supposed to be match but the corresponding information is not provided, \
                       an error will be raised. If the datapoint is successfully added, a notification will be sent to the database to notify the \
                       database that a new datapoint has been added as well as whether the topic needs to be subscribed to.")
async def add_datapoint(datapoint: Datapoint, conn: asyncpg.Connection = Depends(get_connection)):
    if datapoint.matchDatapoint and (datapoint.entity_id is None or datapoint.attribute_name is None):
        raise HTTPException(status_code=400, detail="entity_id and attribute_name must be set if Match Datapoint is enabled!")
    try:
        async with conn.transaction():
            # check if there is already a device subscribed to the same topic
            # if so, the gateway will not subscribe to the topic again
            subscribe = await conn.fetchrow(
                """SELECT object_id FROM datapoints WHERE topic=$1 AND object_id!=$2""",
                datapoint.topic, datapoint.object_id
            )
            await conn.execute(
                """INSERT INTO datapoints (object_id, jsonpath, topic, entity_id, entity_type, attribute_name, description) 
                VALUES ($1, $2, $3, $4, $5, $6, $7)""",
                datapoint.object_id, datapoint.jsonpath, datapoint.topic,
                datapoint.entity_id, datapoint.entity_type, datapoint.attribute_name, 
                datapoint.description
            )
        
        await postgres_notify("add_datapoint", json.dumps({"object_id": datapoint.object_id,
                                                            "jsonpath": datapoint.jsonpath,
                                                            "topic": datapoint.topic,
                                                            "entity_id": datapoint.entity_id,
                                                            "entity_type": datapoint.entity_type,
                                                            "attribute_name": datapoint.attribute_name,
                                                            "subscribe": subscribe is None}), conn)
        return {**datapoint.dict(), "subscribe": subscribe is None}
    
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(status_code=400, detail="Device already exists!")
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error!")

@app.put("/data/{object_id}", response_model=DatapointUpdate,
            summary="Update a specific datapoint in the gateway",
            description="Update a specific datapoint in the gateway. This is to allow the frontend to match a datapoint to an existing entity/attribute pair in the Context Broker.")
async def update_datapoint(object_id: str, datapoint: DatapointUpdate, conn: asyncpg.Connection = Depends(get_connection)):
    await conn.execute(
        """UPDATE datapoints SET entity_id=$1, entity_type=$2, attribute_name=$3, description=$4 WHERE object_id=$5""",
        datapoint.entity_id, datapoint.entity_type,
        datapoint.attribute_name, datapoint.description, 
        object_id
    )
    return {**datapoint.dict()}

@app.delete("/data/{object_id}", status_code=204)
async def delete_datapoint(object_id: str, conn: asyncpg.Connection = Depends(get_connection)):
    """
    Delete a specific datapoint from the database. This is to allow the frontend to delete a datapoint from the gateway.
    """
    try:
        async with conn.transaction():
            datapoint = await conn.fetchrow(
                """SELECT jsonpath, topic, entity_id, entity_type, attribute_name FROM datapoints WHERE object_id=$1""",
                object_id
            )
            # check if the topic is the last subscriber
            # if so, the gateway will unsubscribe from the topic
            unsubscribe = await conn.fetchrow(
                """SELECT object_id FROM datapoints WHERE topic=$1 AND object_id!=$2""",
                datapoint["topic"], object_id
            )
            await conn.execute(
                """DELETE FROM datapoints WHERE object_id=$1""",
                object_id
            )
            
        await postgres_notify("remove_datapoint", json.dumps({"object_id": object_id,
                                                            "jsonpath": datapoint["jsonpath"],
                                                            "topic": datapoint["topic"],
                                                            "entity_id": datapoint["entity_id"],
                                                            "entity_type": datapoint["entity_type"],
                                                            "attribute_name": datapoint["attribute_name"],                                                 
                                                            "unsubscribe": unsubscribe is None}), conn)
        return None
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error!")

@app.get("/data/{object_id}/status", response_model=bool)
async def get_match_status(object_id: str, conn: asyncpg.Connection = Depends(get_connection)):
    """
    Get the match status of a specific datapoint. This is to allow the frontend to check whether a datapoint is matched to an existing entity/attribute pair in the Context Broker.
    """
    row = await conn.fetchrow(
        """SELECT entity_id, attribute_name FROM datapoints WHERE object_id=$1""",
        object_id
    )
    if row is None:
        raise HTTPException(status_code=404, detail="Device not found!")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ORION_URL}/v2/entities/{row['entity_id']}/attrs/{row['attribute_name']}")
        return response.status_code == 200

@app.get("/system/orion/status", response_model=bool)
async def get_orion_status():
    """
    Get the status of the Context Broker. This is to allow the frontend to check whether the Context Broker is reachable.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ORION_URL}/version")
        return response.status_code == 200
    
@app.get("/system/postgres/status", response_model=bool)
async def get_postgres_status(conn: asyncpg.Connection = Depends(get_connection)):
    """
    Get the status of the database. This is to allow the frontend to check whether the database is reachable.
    """
    try:
        await conn.execute("SELECT 1")
        return True
    except:
        raise HTTPException(status_code=500, detail="Database is not reachable!")

@app.get("/system/redis/status", response_model=bool)
async def get_redis_status():
    """
    Get the status of the Redis server. This is to allow the frontend to check whether the Redis server is reachable.
    """
    try:
        await app.state.redis.ping()
        return True
    except:
        raise HTTPException(status_code=500, detail="Redis server is not reachable!")
