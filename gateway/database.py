import uuid

import psycopg2
from psycopg2.extras import register_uuid

class PostgresDB:
    """This class is used to store the names of iot devices and their corresponding topics in a database.
    """
    def __init__(self,
                 host="161.35.205.102", 
                 user="karelia", 
                 password="postgres", 
                 database="iot_gateway"):
        try:
            register_uuid()
            self.connection = psycopg2.connect(host=host, user=user, password=password, database=database)
            self.cursor = self.connection.cursor()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS devices (
                                id UUID PRIMARY KEY,
                                device_id VARCHAR(255) UNIQUE NOT NULL,
                                topic VARCHAR(255) NOT NULL
)
""")
            self.connection.commit()
        except psycopg2.OperationalError as e:
            print(e)
            exit(1)

    
    def add_device(self, device_id, topic):
        """Add a device to the database.

        Args:
            device_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            device_uuid = uuid.uuid4()
            self.cursor.execute("INSERT INTO devices (id, device_id, topic) VALUES (%s, %s, %s)", (device_uuid, device_id, topic))

            self.connection.commit()
        
        except psycopg2.IntegrityError:
            print(f"Device {device_id} already exists!")
            self.connection.rollback()
        
    def get_topic(self, device_id):
        """Get the topic of a device.
        
        Args:
            topic (str): The topic of the device.
        
        Returns:
            str: The id of the device.
        """
        try:
            self.cursor.execute("""SELECT topic FROM devices WHERE device_id=%s""", (device_id,))
            return self.cursor.fetchone()
        except TypeError:
            print(f"Device {device_id} does not exist!")
    
    def get_device_id(self, topic):
        """Get the id of a device.
        
        Args:
            topic (str): The topic of the device.
        
        Returns:
            str: The id of the device.
        """
        try:
            self.cursor.execute("""SELECT device_id FROM devices WHERE topic=%s""", (topic,))
            return self.cursor.fetchone()
        except TypeError:
            print(f"Topic {topic} does not exist!")
            
    def get_all_devices(self):
        """Get all devices from the database."""
        self.cursor.execute("""SELECT * FROM devices""")
        return self.cursor.fetchall()
    
    def delete_device(self, device_id):
        """Delete a device from the database.

        Args:
            device_id (str): The id of the device.
        """
        
        try:
            self.cursor.execute("""DELETE FROM devices WHERE device_id=%s""", (device_id,))
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
            
    def update_device(self, device_id, topic):
        """Update a device in the database.

        Args:
            device_id (str): The id of the device.
            topic (str): The topic of the device.
        """
        try:
            self.cursor.execute("""UPDATE devices SET topic=%s WHERE device_id=%s""", (topic, device_id))
            self.connection.commit()
        except psycopg2.IntegrityError:
            print(f"Device {device_id} does not exist!")
            self.connection.rollback()
            
    def nuke_table(self):
        """Delete the devices table."""
        try:
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
    database = PostgresDB(host="161.35.205.102", user="karelia", password="postgres", database="iot_gateway")
    database.add_device("sensor:001", "sensor___001")
    database.add_device("sensor:002", "sensor___002")
    print(database.get_all_devices())
    database.close()