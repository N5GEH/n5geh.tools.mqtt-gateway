import json
from typing import List, Optional
from uuid import uuid4
import asyncpg
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, Extra, validator
from redis import asyncio as aioredis
import aiohttp
import logging
import re
import time
from settings import settings

app = FastAPI()
# enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Change this to the frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

host = settings.POSTGRES_HOST
user = settings.POSTGRES_USER
password = settings.POSTGRES_PASSWORD
database = settings.POSTGRES_DB
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"
ORION_URL = settings.ORION_URL
REDIS_URL = settings.REDIS_URL
# Configure logging
logging.basicConfig(level=settings.LOG_LEVEL.upper(),
                    format='%(asctime)s %(name)s %(levelname)s: %(message)s')

# Pydantic model
class Datapoint(BaseModel):
    object_id: Optional[str] = Field(None, min_length=1, max_length=255)
    jsonpath: str
    topic: str
    entity_id: Optional[str] = Field(None, min_length=1, max_length=255)
    entity_type: Optional[str] = Field(None, min_length=1, max_length=255)
    attribute_name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = ""
    connected: Optional[bool] = None

    @validator('object_id')
    def validate_object_id(cls, value):
        if value is not None:
            if not re.match(r'^[a-zA-Z0-9_\-:]+$', value):
                raise ValueError('object_id contains invalid characters')
        return value


class DatapointUpdate(BaseModel):
    entity_id: Optional[str] = Field(None, min_length=1, max_length=255)
    entity_type: Optional[str] = Field(None, min_length=1, max_length=255)
    attribute_name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = ""
    connected: Optional[bool] = None

class DatapointPartialUpdate(BaseModel):
    entity_id: Optional[str] = Field(None, min_length=1, max_length=255)
    entity_type: Optional[str] = Field(None, min_length=1, max_length=255)
    attribute_name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = ""
    connected: Optional[bool] = None


@app.on_event("startup")
async def startup():
    """
    Create a pool of connections to the database. This is to ensure that the gateway does not have to create a new connection
    to the database for every request. Instead, it can reuse an existing connection from the pool for efficiency.
    Moreover, create a connection to the redis cache to store the subscriptions to the topics and a connection to another redis cache
    to store the notifications to the database.
    """
    app.state.pool = await asyncpg.create_pool(DATABASE_URL)
    app.state.redis = await aioredis.from_url(
        REDIS_URL + "/0"
    )  # same cache as in the gateway
    app.state.notifier = await aioredis.from_url(
        REDIS_URL + "/1"
    )  # different db for notifications

    async with app.state.pool.acquire() as connection:
        # async with is used to ensure that the connection is released back to the pool after the request is done
        await connection.execute(
            """CREATE TABLE IF NOT EXISTS datapoints (
                object_id TEXT PRIMARY KEY,
                jsonpath TEXT NOT NULL,
                topic TEXT NOT NULL,
                entity_id TEXT,
                entity_type TEXT,
                attribute_name TEXT,
                description TEXT,
                connected BOOLEAN DEFAULT FALSE
            )"""
        )

        # Check if the connected column exists, if not add it
        column_exists = await connection.fetchrow(
            """SELECT column_name FROM information_schema.columns 
               WHERE table_name='datapoints' AND column_name='connected'"""
        )
        if not column_exists:
            await connection.execute(
                """ALTER TABLE datapoints ADD COLUMN connected BOOLEAN DEFAULT FALSE"""
            )


@app.on_event("shutdown")
async def shutdown():
    """
    Close the pool of connections to the PostgreSQL database and the connection to the redis caches.
    """
    await app.state.pool.close()
    await app.state.redis.close()
    await app.state.notifier.close()


async def get_connection():
    """
    Get a connection from the pool of connections to the database. This is to ensure that the gateway does not have to create a new connection
    to the database for every request. Instead, it can reuse an existing connection from the pool for efficiency.
    """
    async with app.state.pool.acquire() as connection:
        # async with is used to ensure that the connection is released back to the pool after the request is done
        # a yield statement is used to return the connection to the caller
        yield connection


@app.get(
    "/data",
    response_model=List[Datapoint],
    summary="Get all datapoints from the gateway",
    description="Get all datapoints from the gateway. This is to allow the frontend to display all the registered datapoints in the database.",
)
async def get_datapoints(conn: asyncpg.Connection = Depends(get_connection)):
    """
    Get all datapoints from the gateway. This is to allow the frontend to display all the registered datapoints in the database.
    """
    rows = await conn.fetch(
        "SELECT object_id, jsonpath, topic, entity_id, entity_type, attribute_name, description, connected FROM datapoints"
    )
    return rows


@app.get(
    "/data/{object_id}",
    response_model=Datapoint,
    summary="Get a specific datapoint from the gateway",
    description="Get a specific datapoint from the gateway. This is to allow the frontend to display a specific datapoint in the database. \
                        If the datapoint is not found, an error will be raised.",
)
async def get_datapoint(
    object_id: str, conn: asyncpg.Connection = Depends(get_connection)
):
    """
    Get a specific datapoint from the gateway. This is to allow the frontend to display a specific datapoint in the database.
    If the datapoint is not found, an error will be raised.

    Args:
        object_id (str): The object_id of the datapoint to be retrieved
        conn (asyncpg.Connection, optional): The connection to the database. Defaults to Depends(get_connection) which is a connection from the pool of connections to the database.

    Raises:
        HTTPException: If the datapoint is not found, a 404 error will be raised.

    """
    row = await conn.fetchrow(
        """SELECT * FROM datapoints WHERE object_id=$1""", object_id
    )
    if row is None:
        raise HTTPException(status_code=404, detail="Device not found!")
    return row



@app.post(
    "/data",
    response_model=Datapoint,
    status_code=201,
    summary="Add a new datapoint to the gateway",
    description="Add a new datapoint to the gateway. This is to allow to add new datapoints to the gateway. \
                       In (a very unlikely) case where the datapoint was supposed to be matched but the corresponding information is not provided, \
                       an error will be raised. If the datapoint is successfully added, a notification will be sent to the database to notify the \
                       database that a new datapoint has been added as well as whether the topic needs to be subscribed to.",
)
async def add_datapoint(
    datapoint: Datapoint, conn: asyncpg.Connection = Depends(get_connection)
):
    """
    Add a new datapoint to the gateway. This is to allow to add new datapoints to the gateway via the frontend.
    In (a very unlikely) case where the datapoint was supposed to be matched but the corresponding information is not provided,
    an error will be raised. If the datapoint is successfully added, a notification will be sent to the database to notify the
    database that a new datapoint has been added as well as whether the topic needs to be subscribed to.

    Args:
        datapoint (Datapoint): The datapoint to be added to the gateway.
        conn (asyncpg.Connection, optional): The connection to the database. Defaults to Depends(get_connection) which is a connection from the pool of connections to the database.

    Raises:
        HTTPException: If the datapoint is supposed to be matched but the corresponding information is not provided, a 400 error will be raised.
        UniqueViolationError: If the object_id of the datapoint already exists in the database, a 409 error will be raised.
        Exception: If some other error occurs, a 500 error will be raised.
    """

    logging.info(f"Received datapoint for addition: {datapoint.json()}")

    # Validate the presence of required fields if connected is True
    if datapoint.connected:
        if not datapoint.entity_id or not datapoint.entity_type or not datapoint.attribute_name:
            raise HTTPException(status_code=400, detail="entity_id, entity_type, and attribute_name cannot be null if connected is True")
        
    # Remove 'connected' field if it is set
    datapoint.connected = None
    
    # Generate a new 6-character object_id if not provided
    if datapoint.object_id is None:
        while True:
            new_id = str(uuid4())[:6]
            existing = await conn.fetchrow(
                """SELECT object_id FROM datapoints WHERE object_id=$1""",
                new_id
            )
            if not existing:
                datapoint.object_id = new_id
                break

    else:
        # Check if the provided object_id is unique
        existing = await conn.fetchrow(
            """SELECT object_id FROM datapoints WHERE object_id=$1""",
            datapoint.object_id
        )
        if existing:
            raise HTTPException(status_code=409, detail="object_id already exists!")

    try:
        async with conn.transaction():
            # check if there is already a device subscribed to the same topic
            # if so, the gateway will not subscribe to the topic again
            subscribed = await conn.fetchrow(
                """SELECT object_id FROM datapoints WHERE topic=$1""",
                datapoint.topic
            )
            await conn.execute(
                """INSERT INTO datapoints (object_id, jsonpath, topic, entity_id, entity_type, attribute_name, description, connected) 
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8)""",
                datapoint.object_id,
                datapoint.jsonpath,
                datapoint.topic,
                datapoint.entity_id,
                datapoint.entity_type,
                datapoint.attribute_name,
                datapoint.description,
                False, # Initially set connected to False
            )

        # store the jsonpath and topic in redis for easy retrieval later
        # await app.state.redis.set(
        #     datapoint.object_id,
        #     json.dumps({"jsonpath": datapoint.jsonpath, "topic": datapoint.topic}),
        # )

        await app.state.redis.hset(
            datapoint.topic,
            datapoint.object_id,
            json.dumps(
                {
                    "object_id": datapoint.object_id,
                    "jsonpath": datapoint.jsonpath,
                    "entity_id": datapoint.entity_id,
                    "entity_type": datapoint.entity_type,
                    "attribute_name": datapoint.attribute_name,
                    "description": datapoint.description,
                    "connected": False,
                }
            ),
        )

        # publish a notification to the database to notify that a new datapoint has been added
        if not subscribed:
            stream_name = "manage_topics"
            await app.state.notifier.xadd(
                stream_name,
                {'subscribe': datapoint.topic},
            )
        # Check if the datapoint can be connected
        await check_and_update_connected(datapoint.object_id, conn)

        return {**datapoint.dict(), "subscribe": subscribed is None}

    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(status_code=409, detail="Device already exists!")

    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error!")


@app.put(
    "/data/{object_id}",
    response_model=DatapointUpdate,
    summary="Update a specific datapoint in the gateway",
    description="Update a specific datapoint in the gateway. This is to allow the frontend to match a datapoint to an existing entity/attribute pair in the Context Broker.",
)
async def update_datapoint(
    object_id: str,
    datapoint: DatapointUpdate,
    conn: asyncpg.Connection = Depends(get_connection),
):
    """
    Update a specific datapoint in the gateway. This is to allow the frontend to match a datapoint to an existing entity/attribute pair in the Context Broker.

    Args:
        object_id (str): The object_id of the datapoint to be updated.
        datapoint (DatapointUpdate): The updated datapoint.
        conn (asyncpg.Connection, optional): The connection to the database. Defaults to Depends(get_connection) which is a connection from the pool of connections to the database.

    Raises:
             HTTPException: If the datapoint is supposed to be matched but the corresponding information is not provided, a 400 error will be raised.
             HTTPException: If the datapoint to be updated is not found, a 404 error will be raised.
             HTTPException: Raises a 422 error if attempts are made to modify the original datapoint's jsonpath or topic.
             Exception: If some other error occurs, a 500 error will be raised.
         """

    # Remove 'connected' field if it is set
    update_data = datapoint.dict(exclude_unset=True)
    if 'connected' in update_data:
        update_data.pop('connected')
                        
    # Add validation to ensure entity_id, entity_type, and attribute_name are not None
    if datapoint.entity_id is None or datapoint.entity_type is None or datapoint.attribute_name is None:
        raise HTTPException(status_code=400, detail="entity_id, entity_type, and attribute_name cannot be null")

    try:
        # Start a transaction to ensure atomicity
        async with conn.transaction():
            
            await conn.execute(
                """UPDATE datapoints SET entity_id=$1, entity_type=$2, attribute_name=$3, description=$4 WHERE object_id=$5""",
                datapoint.entity_id,
                datapoint.entity_type,
                datapoint.attribute_name,
                datapoint.description,
                object_id,
            )

            row = await conn.fetchrow(
                """SELECT jsonpath, topic FROM datapoints WHERE object_id=$1""", object_id
            )

        await app.state.redis.hset(
            row['topic'],
            object_id,
            json.dumps(
                {
                    "object_id": object_id,
                    "jsonpath": row['jsonpath'],
                    "entity_id": update_data.get('entity_id'),
                    "entity_type": update_data.get('entity_type'),
                    "attribute_name": update_data.get('attribute_name'),
                    "description": update_data.get('description'),
                }
            ),
        )

        # Check if the datapoint can be connected
        await check_and_update_connected(object_id, conn)

        return {**datapoint.dict()}

    except Exception as e:
        logging.error(f"Error updating datapoint: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error!")


@app.patch(
    "/data/{object_id}",
    response_model=Datapoint,
    summary="Partially update a specific datapoint in the gateway",
    description="Partially update a specific datapoint in the gateway. This allows the frontend to update specific fields of a datapoint.",
)
async def partial_update_datapoint(
    object_id: str,
    datapoint_update: DatapointPartialUpdate,
    conn: asyncpg.Connection = Depends(get_connection),
):
    existing_datapoint = await conn.fetchrow(
        """SELECT * FROM datapoints WHERE object_id=$1""", object_id
    )
    if existing_datapoint is None:
        raise HTTPException(status_code=404, detail="Datapoint not found!")

    update_data = datapoint_update.dict(exclude_unset=True)

    if 'entity_id' in update_data and 'attribute_name' not in update_data and existing_datapoint['attribute_name'] is None:
        raise HTTPException(
            status_code=400,
            detail="attribute_name must be set if entity_id is provided!",
        )

    if 'attribute_name' in update_data and 'entity_id' not in update_data and existing_datapoint['entity_id'] is None:
        raise HTTPException(
            status_code=400,
            detail="entity_id must be set if attribute_name is provided!",
        )
    
    if 'connected' in update_data:
        update_data.pop('connected')

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No valid fields provided for update.",
        )

    try:
        async with conn.transaction():
            # Dynamically build the SQL query to update only provided fields
            set_clauses = ", ".join([f"{key} = ${i + 1}" for i, key in enumerate(update_data.keys())])
            values = list(update_data.values()) + [object_id]
            query = f"UPDATE datapoints SET {set_clauses} WHERE object_id = ${len(values)}"
            await conn.execute(query, *values)

            # Retrieve updated datapoint
            updated_datapoint = await conn.fetchrow(
                """SELECT * FROM datapoints WHERE object_id=$1""", object_id
            )

            # Update the datapoint in Redis
            await app.state.redis.hset(
                updated_datapoint['topic'],
                object_id,
                json.dumps(
                    {
                        "object_id": object_id,
                        "jsonpath": updated_datapoint['jsonpath'],
                        "entity_id": updated_datapoint['entity_id'],
                        "entity_type": updated_datapoint['entity_type'],
                        "attribute_name": updated_datapoint['attribute_name'],
                        "description": updated_datapoint['description'],
                    }
                ),
            )

        # Check if the datapoint can be connected
        await check_and_update_connected(object_id, conn)

        return updated_datapoint

    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error!")


@app.delete(
    "/data/{object_id}",
    status_code=204,
    summary="Delete a specific datapoint from the gateway",
    description="Delete a specific datapoint from the gateway. This is to allow the frontend to delete a datapoint from the gateway.",
)
async def delete_datapoint(
    object_id: str, conn: asyncpg.Connection = Depends(get_connection)
):
    """
    Delete a specific datapoint from the gateway. This is to allow the frontend to delete a datapoint from the gateway and unsubscribe from the topic if it is the last subscriber.

    Args:
        object_id (str): The object_id of the datapoint to be deleted.
        conn (asyncpg.Connection, optional): The connection to the database. Defaults to Depends(get_connection) which is a connection from the pool of connections to the database.

    Raises:
        Exception: If some error occurs, a 500 error will be raised.
    """
    try:
        async with conn.transaction():
            datapoint = await conn.fetchrow(
                """SELECT jsonpath, topic, entity_id, entity_type, attribute_name FROM datapoints WHERE object_id=$1""",
                object_id,
            )
            # check if the topic is the last subscriber
            # if so, the gateway will unsubscribe from the topic
            unsubscribe = await conn.fetchrow(
                """SELECT object_id FROM datapoints WHERE topic=$1 AND object_id!=$2""",
                datapoint["topic"],
                object_id,
            )
            await conn.execute(
                """DELETE FROM datapoints WHERE object_id=$1""", object_id
            )

        # await app.state.redis.delete(object_id)
        await app.state.redis.hdel(datapoint["topic"], object_id)

        if not unsubscribe:
            # await app.state.notifier.publish("unsubscribe", datapoint["topic"])
            stream_name = "manage_topics"
            await app.state.notifier.xadd(
                stream_name,
                {'unsubscribe': datapoint["topic"]},
            )
        return None
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error!")

@app.delete(
    "/data",
    status_code=204,
    summary="Delete all datapoints from the gateway",
    description="Delete all datapoints from the gateway. This is to allow the frontend to delete all datapoints from the gateway and unsubscribe from all topics.",
)
async def delete_all_datapoints(conn: asyncpg.Connection = Depends(get_connection)):
    """
    Delete all datapoints from the gateway. This is to allow the frontend to delete all datapoints from the gateway and unsubscribe from all topics.

    Args:
        conn (asyncpg.Connection, optional): The connection to the database. Defaults to Depends(get_connection) which is a connection from the pool of connections to the database.

    Raises:
        Exception: If some error occurs, a 500 error will be raised.
    """
    try:
        async with conn.transaction():
            datapoints = await conn.fetch(
                """SELECT object_id, jsonpath, topic FROM datapoints"""
            )
        # notify gateway to unsubscribe all topics
        stream_name = "manage_topics"
        await app.state.notifier.xadd(
            stream_name,
            {'unsubscribe_all': 'all'},
        )
        for datapoint in datapoints:
            await app.state.redis.hdel(datapoint["topic"], datapoint["object_id"])
        return None
    
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error!")

@app.get(
    "/data/{object_id}/status",
    response_model=bool,
    summary="Get the match status of a specific datapoint",
    description="Get the match status of a specific datapoint. This is to allow the frontend to check whether a datapoint is matched to an existing entity/attribute pair in the Context Broker.",
)
async def get_match_status(
    object_id: str, conn: asyncpg.Connection = Depends(get_connection)
):
    """
    Get the match status of a specific datapoint. This is to allow the frontend to check whether a datapoint is matched to an existing entity/attribute pair in the Context Broker.

    Args:
        object_id (str): The object_id of the datapoint to be checked.
        conn (asyncpg.Connection, optional): The connection to the database. Defaults to Depends(get_connection) which is a connection from the pool of connections to the database.

    Raises:
        HTTPException: If the datapoint is not found in the Context Broker, a 404 error will be raised.

    Returns:
        bool: True if the datapoint is matched to an existing entity/attribute pair in the Context Broker, False otherwise.
    """
    row = await conn.fetchrow(
        """SELECT entity_id, entity_type, attribute_name FROM datapoints WHERE object_id=$1""",
        object_id,
    )
    if row is None:
        raise HTTPException(status_code=404, detail="Datapoint not found!")

    async with aiohttp.ClientSession() as session:
        entity_id = row['entity_id']
        attribute_name = row['attribute_name']
        entity_type = row['entity_type']
        url = f"{ORION_URL}/v2/entities/{entity_id}/attrs/{attribute_name}/?type={entity_type}"
        response = await session.get(url)
        match_status = response.status == 200
        logging.info(f"Checking match status for entity_id: {entity_id}, attribute_name: {attribute_name}, entity_type: {entity_type}")
        logging.info(f"Request URL: {url}")
        logging.info(f"Response status: {response.status}")
        return match_status


async def check_and_update_connected(object_id: str, conn: asyncpg.Connection):
    """
    Check if the datapoint can be marked as connected based on the presence of entity_id and attribute_name,
    and update the connected status accordingly.
    """

    # Fetch the entity_id, attribute_name, and entity_type from the datapoints table
    row = await conn.fetchrow(
        """SELECT entity_id, attribute_name, entity_type FROM datapoints WHERE object_id=$1""", object_id
    )

    # Check if entity_id, attribute_name, and entity_type are all present
    if row['entity_id'] and row['attribute_name'] and row['entity_type']:
        async with aiohttp.ClientSession() as session:

            # Construct the URL to query the FIWARE Context Broker
            url = f"{settings.ORION_URL}/v2/entities/{row['entity_id']}/attrs/{row['attribute_name']}?type={row['entity_type']}"

            # Send a GET request to the FIWARE Context Broker
            async with session.get(url) as response:

                # If the response status is 200, the entity and attribute exist
                if response.status == 200:
                    await conn.execute(
                        """UPDATE datapoints SET connected=$1 WHERE object_id=$2""",
                        True,
                        object_id,
                    )

                # If the response status is not 200, the entity or attribute does not exist
                else:
                    await conn.execute(
                        """UPDATE datapoints SET connected=$1 WHERE object_id=$2""",
                        False,
                        object_id,
                    )
                            
    # If any of the entity_id, attribute_name, or entity_type are missing
    else:
        await conn.execute(
            """UPDATE datapoints SET connected=$1 WHERE object_id=$2""",
            False,
            object_id,
        )


@app.get("/system/status",
    response_model=dict,
    summary="Get the status of the system",
    description="Get the status of the system. This is to allow the frontend to check whether the system is running properly.",
)
async def get_status():
    system_status = {
        "orion": await check_orion(),
        "postgres": await check_postgres(),
        "redis": await check_redis(),
    }
    return system_status

async def check_orion():
    """
    Check whether the Orion Context Broker is running properly.
    """
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"{ORION_URL}/version")
            return response.status == 200
    except Exception as e:
        logging.error(f"Error checking Orion: {e}")
        return False

async def check_postgres():
    """
    Check whether the PostgreSQL database is running properly.
    """
    try:
        async with app.state.pool.acquire() as connection:
            await connection.execute("SELECT 1")
            return True
    except Exception as e:
        logging.error(f"Error checking PostgreSQL: {e}")
        return False

async def check_redis():
    """
    Check whether the Redis cache is running properly.
    """
    try:
        await app.state.redis.ping()
        return True
    except Exception as e:
        logging.error(f"Error checking Redis: {e}")
        return False

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True,
                log_level=settings.LOG_LEVEL.lower())