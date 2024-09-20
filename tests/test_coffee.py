import pytest
from coffee import Coffee

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("") 

def test_coffee_num_orders():
    from customer import Customer
    customer = Customer("Jay")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 3.5)  
    assert coffee.num_orders() == 1  
