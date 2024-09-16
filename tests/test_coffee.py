import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Co")
    Coffee("Coffee")

def test_coffee_orders():
    coffee = Coffee("Coffee")
    customer1 = Customer("Sarah")
    customer2 = Customer("Jay")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.orders() == [order1, order2]

def test_coffee_customers():
    coffee = Coffee("Coffee")
    customer1 = Customer("Sarah")
    customer2 = Customer("Jay")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.customers() == {customer1, customer2}

def test_coffee_num_orders():
    coffee = Coffee("Coffee")
    customer = Customer("Sarah")
    order1 = Order(customer, coffee, 3.5)
    order2 = Order(customer, coffee, 4.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Coffee")
    customer = Customer("Sarah")
    order1 = Order(customer, coffee, 5.5)
    order2 = Order(customer, coffee, 5.0)
    assert coffee.average_price() == 5.25