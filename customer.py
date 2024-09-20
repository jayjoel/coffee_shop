from order import Order

class Customer:
    def __init__(self, name):
        if not name or len(name) < 2:
            raise ValueError("Customer name must be at least 2 characters long.")
        self.name = name
        self._orders = []  # Initialize orders list

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)  # Link the order to the coffee
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return {order.coffee.name for order in self._orders}

    @staticmethod
    def most_aficionado(coffee_name):
        """Determines the customer who has ordered the most of a specific coffee."""
        from order import Order
        all_orders = Order.all_orders()
        
        # Filter orders for the specific coffee
        coffee_orders = [order for order in all_orders if order.coffee.name == coffee_name]
        if not coffee_orders:
            return None
        
        # Count how many times each customer has ordered the coffee
        customer_order_count = {}
        for order in coffee_orders:
            customer_order_count[order.customer] = customer_order_count.get(order.customer, 0) + 1
        
        return max(customer_order_count, key=customer_order_count.get)
