class Customer:
    def __init__(self, name):

        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            
            raise ValueError("Invalid customer name")
        
        self._name = name

    @property
    def name(self):
        return self._name

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders() if order.customer == self]

    def coffees(self):
        return set(order.coffee for order in self.orders())

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        orders = [order for order in Order.all_orders() if order.coffee == coffee]
        if not orders:
            return None
        return max(orders, key=lambda order: order.price).customer