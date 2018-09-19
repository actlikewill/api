"""
This is the routes file for directing the user requests
"""

from flask import jsonify, make_response, abort, request
from app import app
from app.models import Orders


USERS = [
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
    """GET users"""
    return jsonify({'users': USERS})

@app.route('/api/users/<string:name>', methods=['GET'])
def get_user(name):
    """GET individual users given the name"""
    user = [user for user in USERS if user['name'] == name]
    if not user:
        abort(404)
    return jsonify({'user': user[0]})

@app.errorhandler(404)
def not_found(e): #pylint: disable=unused-argument, invalid-name
    """Yer basic 404 error handler"""
    return make_response(jsonify({'error': 'Not found'})), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    """ POST users """
    user = {
        "name":request.get_json(force=True)['name'],
        "age":request.get_json(force=True)['age'],
        "occupation":request.get_json(force=True)['occupation']
    }
    USERS.append(user)
    return jsonify({"user": user}), 201

@app.route('/api/users/<string:name>', methods=['DELETE'])
def delete_user(name):
    """DELETE users"""
    user = [user for user in USERS if user['name'] == name]
    if not user:
        abort(404)
    USERS.remove(user[0])
    return jsonify({'result': True})

@app.route('/api/users/<string:name>', methods=['PUT'])
def update_user(name):
    """PUT users"""
    user = [user for user in USERS if user['name'] == name]
    if not user:
        abort(404)
    if not request.json:
        abort(400)
    user[0]['name'] = request.get_json()['name']
    user[0]['age'] = request.get_json()['age']
    user[0]['occupation'] = request.get_json()['occupation']
    return jsonify({'user': user[0]})

@app.route('/orders', methods=['POST', 'GET'])
def my_order():
    """GET orders"""
    if request.method == 'POST':
        order = {
            "item": request.args.get('item'),
            "quantity": request.args.get('quantity')
        }
        ORDERS.add_order(order)
        return jsonify(order), 201
    return jsonify({"orders": ORDERS.order_list})

@app.route('/')
def index():
    """GET index"""
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browseris %s</p>' % user_agent
