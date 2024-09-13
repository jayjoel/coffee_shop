import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_price_validation():
    customer = Customer("Jay")
    with pytest.raises(ValueError):
        Order(customer, "Cappuccino", 1.0)
    with pytest.raises(ValueError):
        Order(customer, "Cappuccino", 9.1)
    Order(customer, "Cappuccino", 6.0)

def test_order_properties():
    customer = Customer("Jay")
    order = Order(customer, "Cappuccino", 4.5)
    assert order.customer == customer
    assert order.coffee == "Cappuccino"
    assert order.price == 4.5

def test_order_all_orders():
    customer1 = Customer("Jay")
    customer2 = Customer("Domie")
    order1 = Order(customer1, "Cappuccino", 4.5)
    order2 = Order(customer2, "Latte", 4.0)
    