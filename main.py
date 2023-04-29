import asyncpg
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: Change this to the frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection settings
DATABASE_URL = "postgres://karelia:postgres@161.35.205.102:5432/iot_gateway"

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
    row = await conn.fetchrow("SELECT id, field1, field2 FROM my_table WHERE id = $1", item_id)
    await close_db(conn)
    if row is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return MyData(**row)
