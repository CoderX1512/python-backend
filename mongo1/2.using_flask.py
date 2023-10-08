from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Step-1: Establish the connection to the MongoDB
# Replace your 'your_mongodb_url' with your MongoDB connection string
client = MongoClient("mongodb://localhost:27017")

db = client.company
collection = db.employees

# CREATE operation
@app.route('/employees',methods=['POST'])
def create_employees():
    data = request.get_json()
    insert_result = collection.insert_one(data)
    return jsonify({"message": "Employee created successfully", "id": str(insert_result.inserted_id)}), 201

# READ operation(Retrieve all employees)
@app.route('/employees',methods=['GET'])
def get_employees():
    employees = list(collection.find())
    for employee in employees:
        employee['_id'] = str(employee['_id'])  # Convert ObjectId to string
    return jsonify(employees), 200


# READ operation(Retrieve a specific employee)
@app.route('/employees/<employee_id>',methods=['GET'])
def get_employee(employee_id):
    employee = collection.find_one({'_id': ObjectId(employee_id)})
    if employee:
        employee['_id'] = str(employee['_id'])  # Convert ObjectId to string
        return jsonify(employee), 200
    else:
        return jsonify({"message":"Employee Not Found"}), 404


# UPDATE Operation
@app.route('/employees/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    update_result = collection.update_one({'_id': ObjectId(employee_id)}, {'$set': data})
    if update_result.modified_count > 0:
        return jsonify({"message": "Employee updated successfully"}), 200
    else:
        return jsonify({"message": "Employee Not Found"}), 404


# DELETE Operation
@app.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    delete_result = collection.delete_one({'_id': ObjectId(employee_id)})
    if delete_result.deleted_count > 0:
        return jsonify({"message": "Employee deleted successfully"}), 200
    else:
        return jsonify({"message": "Employee Not Found"}), 404



if __name__ == '__main__':
    app.run(debug=True)