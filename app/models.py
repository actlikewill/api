

class Order:
    def __init__(self, item_name, item_quantity):
        self.item_name = item_name        
        self.item_quantity = item_quantity



class Orders:
    """This creates the list of orders to be passed"""
    def __init__(self):
        self.order_list = [{'new':'order'}]

    def add_order(self, order_obj):
        new_order_obj = Order(order_obj['item'], order_obj['quantity'])
        new_order = {
            "item": new_order_obj.item_name,
            "quantity": new_order_obj.item_quantity,
            "status": "Pending"
        }        
        self.order_list.append(new_order)


