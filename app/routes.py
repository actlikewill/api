from app import app
from flask import jsonify, make_response, abort, request
from app.models import Orders 


users = [
    {
        'name': "Wilson",
        'age': 30,
        'occupation': 'Farmer'

    },
    {
        'name': "Michael",
        'age':23,
        'occupation': 'Singer'
    },
    {
        'name': "Joseph",
        'age':34,
        'occupation': 'Manager'
    }
]

ORDERS = Orders()




@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.route('/api/users/<string:name>', methods=['GET'])
def get_user(name):
    user = [user for user in users if user['name'] == name]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

@app.route('/api/users', methods=['POST'])
def create_user():
    user = {
        "name":request.get_json(force=True)['name'],
        "age":request.get_json(force=True)['age'],
        "occupation":request.get_json(force=True)['occupation']
    }
    users.append(user)
    return jsonify({"user": user}), 201

@app.route('/api/users/<string:name>', methods=['DELETE'])
def delete_user(name):
    user = [user for user in users if user['name'] == name]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})

@app.route('/api/users/<string:name>', methods=['PUT'])
def update_user(name):
    user = [user for user in users if user['name'] == name]
    if len(name) == 0:
        abort(404)
    if not request.json:
        abort(400)
    user[0]['name'] = request.get_json()['name']
    user[0]['age'] = request.get_json()['age']
    user[0]['occupation'] = request.get_json()['occupation']
    return jsonify({'user': user[0]})

@app.route('/orders', methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        order = {
            "item": request.args.get('item'),
            "quantity": request.args.get('quantity')        
        }
        ORDERS.add_order(order)
        return jsonify(order), 201
    else:
        return jsonify({"orders": ORDERS.order_list})

@app.route('/')
def index():
    return 'Hello World'
