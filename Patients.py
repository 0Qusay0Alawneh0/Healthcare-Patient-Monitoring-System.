from pymongo import MongoClient
from config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client["healthcare"]
patients = db["patients"]

def add_patient(patient):
    patients.insert_one(patient)

def get_patient(pid):
    return patients.find_one({"_id": pid})

def update_patient(pid, update):
    patients.update_one({"_id": pid}, {"$set": update})

def delete_patient(pid):
    patients.delete_one({"_id": pid})

if __name__ == "__main__":
    add_patient({
        "_id": "patient_001",
        "name": "Ahmad Alali",
        "age": 27,
        "region": "North",
        "medical_history": []
    })
    print(get_patient("patient_001"))
