
class Coffee:
    def __init__(self, name):
        if not name or len(name) < 2:
            raise ValueError("Coffee name must be at least 2 characters long.")
        self.name = name
        self._orders = []  

    def add_order(self, order):
        """Adds an order to the coffee's order list."""
        self._orders.append(order)

    def num_orders(self):
        """Returns the number of orders for this coffee."""
        return len(self._orders)
