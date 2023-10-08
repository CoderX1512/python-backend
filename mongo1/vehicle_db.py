from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.vehicle
collection = db.cars

new_document = {
    "model": "Fortuner 4X2",
    "RegNo": 123456,
    "category": "SUV",
    "brandName":"Toyota"
}
insert_result = collection.insert_one(new_document)
print("Inserted document ID:", insert_result.inserted_id)

# READ operation
# find and print all the documents in the collection
print("Print all the documents in the collection:")
cursor = collection.find()
for document in cursor:
    print(document)