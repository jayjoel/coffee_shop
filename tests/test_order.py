import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
    """Clears the orders list before each test."""
    Order.all_orders_list.clear()

def test_order_all_orders():
    customer1 = Customer("Jay")
    customer2 = Customer("Domie")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Latte")
    order1 = Order(customer1, coffee1, 4.5)
    order2 = Order(customer2, coffee2, 4.0)

    assert Order.all_orders() == [order1, order2]  
