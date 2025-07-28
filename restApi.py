from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

store = {}

@app.route('/user/<string:user_id>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'])
def user_handler(user_id):
    if request.method == 'GET':
        user = store.get(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({'error': 'User not found'}), 404

    elif request.method == 'POST':
        if user_id in store:
            return jsonify({'error': 'User already exists'}), 400
        data = request.get_json()
        if not data or 'name' not in data or 'age' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        store[user_id] = {'name': data['name'], 'age': data['age']}
        return jsonify({'message': 'User created', 'user': store[user_id]}), 201

    elif request.method == 'PUT':
        data = request.get_json()
        if not data or 'name' not in data or 'age' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        store[user_id] = {'name': data['name'], 'age': data['age']}
        return jsonify({'message': 'User replaced', 'user': store[user_id]}), 200

    elif request.method == 'PATCH':
        user = store.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        data = request.get_json()
        user.update({k: v for k, v in data.items() if k in user})
        return jsonify({'message': 'User updated', 'user': user}), 200

    elif request.method == 'DELETE':
        if user_id in store:
            del store[user_id]
            return jsonify({'message': 'User deleted'}), 200
        return jsonify({'error': 'User not found'}), 404

    elif request.method == 'HEAD':
        if user_id in store:
            return '', 200
        return '', 404

    elif request.method == 'OPTIONS':
        return make_response('', 204, {
            'Allow': 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        })

if __name__ == '__main__':
    app.run(port=8000, debug=True)
