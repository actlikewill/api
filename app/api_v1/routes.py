from flask import jsonify, request, render_template
from . import  api_v1
from flask_restful import Resource, Api
from .models import Orders

api = Api(api_v1)

ORDERS = Orders()


class GetOrders(Resource):
    def get(self):
        if len(ORDERS.order_list) == 0:
            return {"sorry": "no orders yet"}, 200, {'Access-Control-Allow-Origin': 'origin-list-or-null'}
        return {'Orders': ORDERS.order_list}, 200, {'Access-Control-Allow-Origin': 'null'}

    def post(self):
        if not request.args:
            return jsonify({"sorry":"no arguments passed"})
        if not request.args.get('item'):
            return jsonify({"sorry":"no item argument passed"})
        if not request.args.get('quantity'):
            return jsonify({"sorry":"no quantity argument passed"})
        order = {
            "item": request.args.get('item'),
            "quantity": request.args.get('quantity'),
            "order_id":len(ORDERS.order_list) + 1,
            "status": "Pending"
        }
        ORDERS.add_order(order)
        return {"Order Placed": order}, 201




api.add_resource(GetOrders, '/orders')

@api_v1.route('/')
def index():
    return render_template('index.html')

@api_v1.route('/')
def hello():
    return "hello"




