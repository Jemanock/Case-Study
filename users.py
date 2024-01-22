import os
from tinydb import TinyDB, Query
from serializer import serializer

class User:
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')
    def __init__(self, id, name) -> None:
        self.name = name
        self.id = id

    def store_data(self):
        print("Storing user...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.name == self.name)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")

if __name__ == "__main__":
    # Create a device
    user1 = User("User1", "one@mci.edu")
    user2 = User("User2", "two@mci.edu") 
    user3 = User("User3", "two@mci.edu") 
    user1.store_data()
    user2.store_data()
    user3.store_data()


    loaded_users = User.load_data_by_device_name('Device2')
    if loaded_users:
        print(f"Loaded Device: {loaded_users}")
    else:
        print("Device not found.")
        
