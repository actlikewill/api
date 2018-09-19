"""
This file creates the order class which lays out the basic structure
of the order table
"""

class Orders:
    def __init__(self):
        self.order_list = []

    def add_order(self, order):        
        self.order_list.append(order)

