import sqlite3

class Database:
    """This class is used to store the names of iot devices and their corresponding topics in a database.
    """
    def __init__(self) -> None:
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS devices (device_id text, topic text)''')
        self.connection.commit()
        
    def add_device(self, device_id, topic):
        try:
            self.cursor.execute('''INSERT INTO devices VALUES (?, ?)''', (device_id, topic))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Device {device_id} already exists!")
                    
    def get_topic(self, device_id):
        try:
            self.cursor.execute('''SELECT topic FROM devices WHERE device_id=?''', (device_id,))
            return self.cursor.fetchone()[0]
        except TypeError:
            print(f"Device {device_id} does not exist!")
    
    def get_device_id(self, topic):
        try:
            self.cursor.execute('''SELECT device_id FROM devices WHERE topic=?''', (topic,))
            return self.cursor.fetchone()[0]
        except TypeError:
            print(f"Topic {topic} does not exist!")
    
    def get_all_devices(self):
        self.cursor.execute('''SELECT * FROM devices''')
        return self.cursor.fetchall()
    
    def delete_device(self, device_id):
        try:
            self.cursor.execute('''DELETE FROM devices WHERE device_id=?''', (device_id,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Device {device_id} does not exist!")
        
    def delete_all_devices(self):
        self.cursor.execute('''DELETE FROM devices''')
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        
    def __del__(self):
        self.close()
        
if __name__ == "__main__":
    database = Database()
    database.add_device("sensor:001", "sensor___001")
    database.add_device("sensor:002", "sensor___002")
    print(database.get_all_devices())
    database.delete_device("sensor:001")
    print(database.get_all_devices())
    database.delete_all_devices()
    print(database.get_all_devices())
    