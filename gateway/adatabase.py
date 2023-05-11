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
        async with self.pool.acquire() as conn:
            await conn.execute(
                """CREATE TABLE IF NOT EXISTS devices (
                                object_id VARCHAR(255) NOT NULL PRIMARY KEY,
                                jsonpath VARCHAR(255) NOT NULL,
                                topic VARCHAR(255) NOT NULL
)
"""
            )
            await conn.add_listener("add_datapoint", self.handle_notify)
            await conn.add_listener("remove_datapoint", self.handle_notify)

    async def handle_notify(self, conn, pid, channel, payload):
        print(f"Got NOTIFY: {pid}, {channel}, {payload}")

    async def get_object_id(self, jsonpath, topic):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """SELECT object_id FROM devices WHERE jsonpath=$1 AND topic=$2""",
                jsonpath, topic,
            )
            return row["object_id"] if row else None

    async def get_all_datapoints(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch("""SELECT object_id, jsonpath, topic FROM devices""")

    async def get_all_topics(self):
        async with self.pool.acquire() as conn:
            return await conn.fetch("""SELECT topic FROM devices""")

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
        await self.pool.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def __del__(self):
        asyncio.run(self.close())


if __name__ == "__main__":
    database = PostgresDB()
