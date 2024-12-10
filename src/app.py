from flask import Flask
from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

todos = [
    { "label": "Walk the dog", "done": False },
    { "label": "Hang the clothes", "done": False },
    { "label": "Make food", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  
    return jsonify(todos)  

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    if 0 <= position < len(todos):
       todos.pop(position)
    else:
       return jsonify({"error": "Invalid position"}), 400

    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)