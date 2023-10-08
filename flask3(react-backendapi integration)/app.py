from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)       # Configure CORS for your app

# Sample lists of tasks
tasks = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Finish Project"},
]

@app.route('/tasks',methods=['GET','POST'])
def handle_tasks():
    if request.method == 'GET':
        return jsonify(tasks)
    elif request.method == 'POST':
        new_task = request.json
        tasks.append(new_task)
        return jsonify({"message": "Task added successfully "}), 201

if __name__ == "__main__":
    app.run(debug=True)