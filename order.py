class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float) or price < 1.0 or price > 9.0:
            raise ValueError("Invalid price. Must be between 0 and 9")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all_orders(cls):
        return cls.orders