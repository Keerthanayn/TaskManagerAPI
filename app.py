from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Learn REST API",
        "status": "Completed"
    }
]


# GET API
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


# POST API
@app.route('/tasks', methods=['POST'])
def add_task():

    new_task = request.get_json()

    new_task["id"] = max(
        [task["id"] for task in tasks],
        default=0
    ) + 1

    tasks.append(new_task)

    return jsonify(new_task), 201

# GET API - Get one task using ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):

    for task in tasks:

        if task["id"] == task_id:
            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404

# PUT API - Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):

    updated_task = request.get_json()

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = updated_task["title"]
            task["status"] = updated_task["status"]

            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404

# PATCH API - Update selected fields
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def patch_task(task_id):

    updated_data = request.get_json()

    for task in tasks:

        if task["id"] == task_id:

            if "title" in updated_data:
                task["title"] = updated_data["title"]

            if "status" in updated_data:
                task["status"] = updated_data["status"]

            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404

# DELETE API - Delete an existing task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return jsonify({
                "message": "Task deleted successfully"
            }), 200

    return jsonify({
        "error": "Task not found"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)