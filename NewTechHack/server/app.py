from flask import Flask, jsonify, request
from flask_cors import CORS

todos = {}
next_id = 1

app = Flask(__name__)
CORS(app)

@app.route('/todos', methods=['GET', 'POST'])
def get_todos():

    if request.method == 'POST':
        
        global next_id
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Bad Request"}), 400
        
        todo = {
            "id": next_id,
            "message": data['message'],
            "completed": data.get('completed', False)
        }

        todos[next_id] = todo
        next_id += 1
        return jsonify(todo), 201

    else:
        return jsonify(list(todos.values())), 200


@app.route('/todos/<int:todo_id>', methods=['GET', 'DELETE', 'PUT'])
def get_todo(todo_id):

    if request.method == 'PUT':
        data = request.get_json()
        todo = todos.get(todo_id)
        if not todo:
            return jsonify({"error": "Not found!"}), 404
        if 'message' in data:
            todo['message'] = data['message']
        if 'completed' in data:
            todo['completed'] = data['completed']
        return jsonify(todo), 200

    if request.method == 'DELETE':
        if todo_id not in todos:
            return jsonify({"error": "Not found"}), 404
        del todos[todo_id]
        return '', 204
    
    else:
        todo = todos.get(todo_id)
        if not todo:
            return jsonify({"error": "Not Found"}), 404
        
        return jsonify(todo), 200

if __name__ == '__main__':
    app.run(debug=True)