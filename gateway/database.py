# Interacts with the PostgreSQL database

import json
import psycopg2
from psycopg2.extras import register_uuid
from psycopg2.pool import SimpleConnectionPool


class PostgresDB:
    """This class is used to store the names of iot devices and their corresponding topics in a database."""

    def __init__(self):
        try:
            config = json.load(open("config.json"))
            self.connection = psycopg2.connect(
                host=config["postgres_setup"]["host"],
                user=config["postgres_setup"]["user"],
                password=config["postgres_setup"]["password"],
                database=config["postgres_setup"]["database"],
            )
            register_uuid()
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True  # Needed for LISTEN to work
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS devices (
                                object_id VARCHAR(255) NOT NULL PRIMARY KEY,
                                jsonpath VARCHAR(255) NOT NULL,
                                topic VARCHAR(255) NOT NULL
)
"""
            )
            self.connection.commit()
        except psycopg2.OperationalError as e:
            print(e)
            exit(1)

    def add_datapoint(self, object_id, jsonpath, topic):
        """Add a device to the database.

        Args:
            object_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            self.cursor.execute(
                """INSERT INTO devices (object_id, jsonpath, topic) VALUES (%s, %s, %s)""",
                (object_id, jsonpath, topic),
            )

            self.connection.commit()

        except psycopg2.IntegrityError:
            print(f"Device {object_id} already exists!")
            self.connection.rollback()

    def get_jsonpath(self, object_id, topic):
        """Get the jsonpath of a device.

        Args:
            topic (str): The topic of the device.

        Returns:
            str: The id of the device.
        """
        try:
            self.cursor.execute(
                """SELECT jsonpath FROM devices WHERE object_id=%s AND topic=%s""",
                (object_id, topic),
            )
            return self.cursor.fetchone()
        except TypeError:
            print(f"Device {object_id} does not exist!")

    def get_topic(self, object_id):
        """Get the topic of a device.

        Args:
            object_id (str): The id of the device.

        Returns:
            str: The topic of the device.
        """
        try:
            self.cursor.execute(
                """SELECT topic FROM devices WHERE object_id=%s""", (object_id,)
            )
            return self.cursor.fetchone()
        except TypeError:
            print(f"Device {object_id} does not exist!")

    def get_object_id(self, jsonpath, topic):
        """Get the id of a device.

        Args:
            topic (str): The topic of the device.

        Returns:
            str: The id of the device.
        """
        try:
            self.cursor.execute(
                """SELECT object_id FROM devices WHERE jsonpath=%s AND topic=%s""",
                (jsonpath, topic),
            )
            return self.cursor.fetchone()
        except TypeError:
            print("Device does not exist!")

    def get_all_datapoints(self):
        """Get all datapoints from the database."""
        self.cursor.execute("""SELECT object_id, jsonpath, topic FROM devices""")
        return self.cursor.fetchall()
        
    def get_all_topics(self):
        """Get all topics from the database."""
        self.cursor.execute("""SELECT topic FROM devices""")
        return self.cursor.fetchall()
    
    def get_jsonpath_and_topic(self, object_id):
        """Get the jsonpath and topic of a device.

        Args:
            object_id (str): The id of the device.

        Returns:
            str: The jsonpath and topic of the device.
        """
        try:
            self.cursor.execute(
                """SELECT jsonpath, topic FROM devices WHERE object_id=%s""", (object_id,)
            )
            return self.cursor.fetchone()
        except TypeError:
            print(f"Device {object_id} does not exist!")
    
    def get_datapoint(self, topic: str):
        """Get the object id and topic of a device.

        Args:
            jsonpath (str): The jsonpath of the device.

        Returns:
            str: The object id and topic of the device.
        """
        try:
            self.cursor.execute(
                """SELECT object_id, jsonpath FROM devices WHERE topic=%s""", (topic,)
            )
            return self.cursor.fetchall()
        except TypeError:
            print(f"The topic {topic} does not exist!")

    def delete_device(self, object_id, topic):
        """Delete a device from the database.

        Args:
            object_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            self.cursor.execute(
                """DELETE FROM devices WHERE object_id=%s AND topic=%s""",
                (object_id, topic),
            )
            self.connection.commit()
        except psycopg2.IntegrityError:
            print(f"Device {object_id} does not exist!")
            self.connection.rollback()

    def delete_all_devices(self):
        """Delete all devices from the database."""
        try:
            self.cursor.execute("""DELETE FROM devices""")
            self.connection.commit()
        except psycopg2.IntegrityError:
            print("No devices to delete!")
            self.connection.rollback()

    def update_device(self, jsonpath, topic, object_id):
        """Update a device in the database.

        Args:
            object_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            self.cursor.execute(
                """UPDATE devices SET jsonpath=%s, topic=%s WHERE object_id=%s""",
                (jsonpath, topic, object_id),
            )
            self.connection.commit()
        except psycopg2.IntegrityError:
            print(f"Device {object_id} does not exist!")
            self.connection.rollback()

    def check_topic(self, topic: str) -> bool:
        """Check if a topic exists in the database.

        Args:
            topic (str): The topic of the device.
        """
        self.cursor.execute(
            """SELECT EXISTS(SELECT 1 FROM devices WHERE topic=%s)""", (topic,)
        )
        return True if self.cursor.fetchone()[0] else False

    def nuke_table(self):
        """Delete the devices table."""
        try:
            print("This will delete the devices table! Are you sure? (y/N)")
            if input() != "y":
                print("Aborting...")
                return
            self.cursor.execute("""DROP TABLE devices""")
            self.connection.commit()
        except psycopg2.IntegrityError:
            print("Table does not exist!")
            self.connection.rollback()

    def close(self):
        """Close the connection to the database."""
        self.connection.close()
        self.cursor.close()

    def __del__(self):
        self.close()


if __name__ == "__main__":
    database = PostgresDB()
