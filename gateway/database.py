import uuid
import json
import psycopg2
from psycopg2.extras import register_uuid

class PostgresDB:
    """This class is used to store the names of iot devices and their corresponding topics in a database.
    """
    def __init__(self):
        try:
            with open("config.json") as f:
                config = json.load(f) 
                self.connection = psycopg2.connect(host=config["postgres_setup"]["host"],
                                                   user=config["postgres_setup"]["user"], 
                                                   password=config["postgres_setup"]["password"], 
                                                   database=config["postgres_setup"]["database"])
            register_uuid()
            self.cursor = self.connection.cursor()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS devices (
                                id UUID PRIMARY KEY,
                                device_id VARCHAR(255) NOT NULL,
                                jsonpath VARCHAR(255) NOT NULL,
                                topic VARCHAR(255) NOT NULL
)
""")
            self.connection.commit()
        except psycopg2.OperationalError as e:
            print(e)
            exit(1)

    
    def add_device(self, device_id, jsonpath, topic):
        """Add a device to the database.

        Args:
            device_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            device_uuid = uuid.uuid4()
            self.cursor.execute("""INSERT INTO devices (id, device_id, jsonpath, topic) VALUES (%s, %s, %s, %s)""", (device_uuid, device_id, jsonpath, topic))

            self.connection.commit()
        
        except psycopg2.IntegrityError:
            print(f"Device {device_id} already exists!")
            self.connection.rollback()
            
    def get_jsonpath(self, device_id, topic):
        """Get the jsonpath of a device.
        
        Args:
            topic (str): The topic of the device.
        
        Returns:
            str: The id of the device.
        """
        try:
            self.cursor.execute("""SELECT jsonpath FROM devices WHERE device_id=%s AND topic=%s""", (device_id, topic))
            return self.cursor.fetchone()
        except TypeError:
            print(f"Device {device_id} does not exist!")
        
    def get_topic(self, device_id):
        """Get the topic of a device.
        
        Args:
            device_id (str): The id of the device.
        
        Returns:
            str: The topic of the device.
        """
        try:
            self.cursor.execute("""SELECT topic FROM devices WHERE device_id=%s""", (device_id,))
            return self.cursor.fetchone()
        except TypeError:
            print(f"Device {device_id} does not exist!")
    
    def get_device_id(self, jsonpath, topic):
        """Get the id of a device.
        
        Args:
            topic (str): The topic of the device.
        
        Returns:
            str: The id of the device.
        """
        try:
            self.cursor.execute("""SELECT device_id FROM devices WHERE jsonpath=%s AND topic=%s""", (jsonpath, topic))
            return self.cursor.fetchone()
        except TypeError:
            print("Device does not exist!")
            
    def get_all_devices(self):
        """Get all devices from the database."""
        self.cursor.execute("""SELECT * FROM devices""")
        return self.cursor.fetchall()
    
    def delete_device(self, device_id, topic):
        """Delete a device from the database.

        Args:
            device_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            self.cursor.execute("""DELETE FROM devices WHERE device_id=%s AND topic=%s""", (device_id, topic))
            self.connection.commit()
        except psycopg2.IntegrityError:
            print(f"Device {device_id} does not exist!")
            self.connection.rollback()
    
    def delete_all_devices(self):
        """Delete all devices from the database."""
        try: 
            self.cursor.execute("""DELETE FROM devices""")
            self.connection.commit()
        except psycopg2.IntegrityError:
            print("No devices to delete!")
            self.connection.rollback()
            
    def update_device(self, jsonpath, topic, device_id):
        """Update a device in the database.

        Args:
            device_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            self.cursor.execute("""UPDATE devices SET jsonpath=%s, topic=%s WHERE device_id=%s""", (jsonpath, topic, device_id))
            self.connection.commit()
        except psycopg2.IntegrityError:
            print(f"Device {device_id} does not exist!")
            self.connection.rollback()
            
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
        """Close the connection to the database.
        """
        self.connection.close()
        self.cursor.close()
        
    
    def __del__(self):
        self.close()

if __name__ == "__main__":
    database = PostgresDB()
    database.nuke_table()