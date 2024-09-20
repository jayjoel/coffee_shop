import pytest
from customer import Customer
from coffee import Coffee
from order import Order  

def test_customer_most_aficionado():
    customer1 = Customer("Jay")
    customer2 = Customer("Alex")
    coffee = Coffee("Cappuccino")
    customer1.create_order(coffee, 3.5)  
    customer2.create_order(coffee, 4.0)   
    customer2.create_order(coffee, 4.5)   
    assert Customer.most_aficionado("Cappuccino") == customer2  
