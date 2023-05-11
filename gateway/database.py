import json
import asyncio
import asyncpg

class PostgresDB:
    def __init__(self):
        self.pool = None
        self.config = json.load(open("config.json"))
        asyncio.run(self.init())

    async def init(self):
        self.pool = await asyncpg.create_pool(
            host=self.config["postgres_setup"]["host"],
            user=self.config["postgres_setup"]["user"],
            password=self.config["postgres_setup"]["password"],
            database=self.config["postgres_setup"]["database"],
        )

    async def add_datapoint(self, object_id, jsonpath, topic):
        async with self.pool.acquire() as conn:
            try:
                await conn.execute(
                    """INSERT INTO devices (object_id, jsonpath, topic) VALUES ($1, $2, $3)""",
                    object_id, jsonpath, topic,
                )
            except asyncpg.exceptions.UniqueViolationError:
                print(f"Device {object_id} already exists!")

    async def get_jsonpath(self, object_id, topic):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """SELECT jsonpath FROM devices WHERE object_id=$1 AND topic=$2""",
                object_id, topic,
            )
            return row["jsonpath"] if row else None

    async def get_topic(self, object_id):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """SELECT topic FROM devices WHERE object_id=$1""", object_id
            )
            return row["topic"] if row else None

    # ... (Add the rest of the methods here, adapted to asyncpg) ...


    async def close(self):
        await self.pool.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def __del__(self):
        asyncio.run(self.close())


if __name__ == "__main__":
    database = PostgresDB()
