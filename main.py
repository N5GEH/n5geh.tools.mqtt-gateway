import asyncpg
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Change this to the frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = json.load(open("config.json"))
host = config["postgres_setup"]["host"]
user = config["postgres_setup"]["user"]
password = config["postgres_setup"]["password"]
database = config["postgres_setup"]["database"]


# Database connection settings
DATABASE_URL = f"postgres://{user}:{password}@{host}:5432/{database}"


async def connect_db():
    connection = await asyncpg.connect(DATABASE_URL)
    return connection


async def close_db(connection):
    await connection.close()


# Pydantic model for the data
class MyData(BaseModel):
    object_id: str
    jsonpath: str
    topic: str


# Fetch all data from the database
@app.get("/data", response_model=List[MyData])
async def get_all_data(conn: asyncpg.Connection = Depends(connect_db)):
    data = await conn.fetch("SELECT object_id, jsonpath, topic FROM devices")
    await close_db(conn)
    return [MyData(**row) for row in data]


# Fetch data by id from the database
@app.get("/data/{item_id}", response_model=MyData)
async def get_data_by_id(item_id: int, conn: asyncpg.Connection = Depends(connect_db)):
    row = await conn.fetchrow(
        "SELECT id, field1, field2 FROM my_table WHERE id = $1", item_id
    )
    await close_db(conn)
    if row is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return MyData(**row)


@app.post("/data", response_model=MyData, status_code=201)
async def add_data(item: MyData, conn: asyncpg.Connection = Depends(connect_db)):
    row = await conn.fetchrow(
        "INSERT INTO devices (object_id, jsonpath, topic) VALUES ($1, $2, $3) RETURNING *",
        item.object_id,
        item.jsonpath,
        item.topic,
    )
    await close_db(conn)
    return MyData(**row)


@app.delete("/data/{object_id}", status_code=204)
async def delete_data(object_id: str, conn: asyncpg.Connection = Depends(connect_db)):
    await conn.execute("DELETE FROM devices WHERE object_id = $1", object_id)
    await close_db(conn)
