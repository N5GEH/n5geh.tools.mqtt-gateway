import json
import asyncio
import asyncpg

class PostgresDB:
    def __init__(self):
        self.pool = None

    async def init(self):
        self.config = json.load(open("config.json"))
        self.pool = await asyncpg.create_pool(
            host=self.config["postgres_setup"]["host"],
            user=self.config["postgres_setup"]["user"],
            password=self.config["postgres_setup"]["password"],
            database=self.config["postgres_setup"]["database"],
        )
        async with self.pool.acquire() as conn:
            await conn.execute(
                """CREATE TABLE IF NOT EXISTS devices (
                                object_id VARCHAR(255) NOT NULL PRIMARY KEY,
                                jsonpath VARCHAR(255) NOT NULL,
                                topic VARCHAR(255) NOT NULL,
                                entity_id VARCHAR(255),
                                attribute_name VARCHAR(255),
                                description VARCHAR(255),
                                matched BOOLEAN NOT NULL DEFAULT FALSE
)
"""
            )

    async def get_object_id(self, jsonpath, topic):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """SELECT object_id FROM devices WHERE jsonpath=$1 AND topic=$2""",
                jsonpath, topic,
            )
            return row["object_id"] if row else None
        
    async def get_mapping(self, jsonpath, topic):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """SELECT entity_id, attribute_name FROM devices WHERE jsonpath=$1 AND topic=$2""",
                jsonpath, topic,
            )
            return (row["entity_id"], row["attribute_name"]) if row else None

    async def get_all_datapoints(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch("""SELECT object_id, jsonpath, topic FROM devices""")

    async def get_all_topics(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch("""SELECT topic FROM devices""")
        
    async def get_all_unique_topics(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch("""SELECT DISTINCT topic FROM devices""")

    async def get_jsonpath_and_topic(self, object_id):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """SELECT jsonpath, topic FROM devices WHERE object_id=$1""", object_id
            )
            return (row["jsonpath"], row["topic"]) if row else None

    async def get_datapoint(self, topic):
        async with self.pool.acquire() as conn:
            return await conn.fetch(
                """SELECT object_id, jsonpath FROM devices WHERE topic=$1""", topic
            )

    async def delete_device(self, object_id, topic):
        async with self.pool.acquire() as conn:
            result = await conn.execute(
                """DELETE FROM devices WHERE object_id=$1 AND topic=$2""",
                object_id, topic,
            )
            if result == "DELETE 0":
                print(f"Device {object_id} does not exist!")

    async def delete_all_devices(self):
        async with self.pool.acquire() as conn:
            await conn.execute("""DELETE FROM devices""")

    async def update_device(self, jsonpath, topic, object_id):
        async with self.pool.acquire() as conn:
            result = await conn.execute(
                """UPDATE devices SET jsonpath=$1, topic=$2 WHERE object_id=$3""",
                jsonpath, topic, object_id,
            )
            if result == "UPDATE 0":
                print(f"Device {object_id} does not exist!")

    async def check_topic(self, topic):
        async with self.pool.acquire() as conn:
            exists = await conn.fetchval(
                """SELECT EXISTS(SELECT 1 FROM devices WHERE topic=$1)""", topic
            )
            return exists

    async def nuke_table(self):
        print("This will delete the devices table! Are you sure? (y/N)")
        if input() != "y":
            print("Aborting...")
            return
        async with self.pool.acquire() as conn:
            await conn.execute("""DROP TABLE devices""")

    async def close(self):
        await self.pool.close() if self.pool else None

    async def __aenter__(self):
        """
        The aenter method is called when the `async with` statement is used. It stands for asynchronous enter.
        As the name suggests, it is called when entering the `async with` statement.
        """
        await self.init()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        The aexit method is called when the `async with` statement is used. It stands for asynchronous exit.
        As the name suggests, it is called when exiting the `async with` statement.
        
        Args (for future reference if needed):
            exc_type: The exception type.
            exc_val: The exception value.
            exc_tb: The exception traceback.
            
        """
        await self.close()

async def get_all_datapoints():
    async with PostgresDB() as db:
        await db.init()
        return await db.get_all_datapoints()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    x = loop.run_until_complete(get_all_datapoints())
    print(x)
    loop.close()