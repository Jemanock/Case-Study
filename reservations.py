import os

from users import User
from devices import Device

from tinydb import TinyDB, Query
from serializer import serializer
import pandas as pd

class Reservation():
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('reservations')

    def __init__(self, res_id, start_date, start_time, end_date, end_time, device_name : str, name : str):
        self.res_id = res_id
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.device_name = device_name
        self.name = name 
        
        self.is_active = True

    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.res_id == self.res_id)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the reservation doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")

    def delete_data(self):
        print("Deleting data...")
        # Check if the device already exists in the database
        ReservationQuery = Query()
        result = self.db_connector.search(ReservationQuery.res_id == self.res_id)
        if result:
            # Delete the existing record
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print("Data deleted.")
        else:
            print("Data not found for deletion.")

    def print(self):
        return f'Reservation Details: {self.res_id}'
        

    @classmethod
    def load_data_by_res_name(cls, res_id):
        # Load data from the database and create an instance of the Device class
        ResQuery = Query()
        result = cls.db_connector.search(ResQuery.res_id == res_id)

        if result:
            data = result[0]
            return cls(data['res_id'], data['start_date'], data['start_time'], data['end_date'], data['end_time'], data['device_name'], data['name'])
        else:
            return None
   
    @classmethod
    def load_all(cls):
        
        all = cls.db_connector.all()
        data = [entry for entry in all]
        df = pd.DataFrame(data)
        df = df.drop(columns=['is_active'])
        df = df.rename(columns={'res_id': 'Reservation ID', 'start_date': 'Start Date', 'start_time': 'Start Time', 'end_date': 'End Date', 'end_time': 'End Time', 'device_name': 'Device', 'name': 'User'})
        df = df.iloc[:, [0, 5, 6, 1, 2, 3, 4]]
        return df

if __name__ == "__main__":
    print("Test")
    print(Reservation.load_all())