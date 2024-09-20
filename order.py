
class Order:
    all_orders_list = []  

    def __init__(self, customer, coffee, price):
        if price < 1.0 or price > 9.0:  
            raise ValueError("Price must be between 1.0 and 9.0")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders_list.append(self)  

    @classmethod
    def all_orders(cls):
        return cls.all_orders_list

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return (self.customer == other.customer and
                self.coffee == other.coffee and
                self.price == other.price)

    def __repr__(self):
        return f"Order(customer={self.customer}, coffee={self.coffee}, price={self.price})"
