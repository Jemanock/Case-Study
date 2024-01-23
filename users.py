import os

from tinydb import TinyDB, Query
from serializer import serializer
#from devices import Device 

class User():
    # Class variable that is shared between all instances of the class
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        
    # String representation of the class
    def __str__(self):
        return f'User {self.username} ({self.email})'

    # String representation of the class
    def __repr__(self):
        return self.__str__()
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.username == self.username)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")

    def delete_data(self):
        print("Deleting data...")
        # Check if the device already exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.username == self.username)
        if result: 
            # Delete the existing record
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print("Data deleted.")
        else:
            print("Data not found for deletion.")


    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def load_data_by_user_name(cls, username):
        # Load data from the database and create an instance of the Device class
        UserQuery = Query()
        result = cls.db_connector.search(UserQuery.username == username)

        if result:
            data = result[0]
            return cls(data['username'], data['email'])
        else:
            return None



if __name__ == "__main__":
    # Create a device
    user1 = User("User1", "one@mci.edu")
    user2 = User("User2", "two@mci.edu") 
    user3 = User("User3", "two@mci.edu") 
    user1.store_data()
    user2.store_data()
    user3.store_data()
    user4 = User("User3", "four@mci.edu") 
    user4.store_data()

    loaded_user = User.load_data_by_user_name('User2')
    if loaded_user:
        print(f"Loaded User: {loaded_user}")
    else:
        print("User not found.")