import logging
from customer import Customer
from coffee import Coffee
from order import Order

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_classes():
    logging.info("Testing Classes")

    try:
        joseph = Customer("Joseph")
        robbin = Customer("Robbin")
        logging.info(f"Customer created: {joseph.name}, {robbin.name}")

        try:
            invalid_customer = Customer("")
        except ValueError as e:
            logging.error(f"Customer error: {e}")
        
    except Exception as e:
        logging.error(f"Error: {e}")

    try:
        espresso = Coffee("Espresso")
        latte = Coffee("Latte")
        logging.info(f"Coffee created: {espresso.name}, {latte.name}")

        try:
            invalid_coffee = Coffee("A")
        except ValueError as e:
            logging.error(f"Coffee error: {e}")

    except Exception as e:
        logging.error(f"Error: {e}")

    try:
        joseph = Customer("Joseph")
        espresso = Coffee("Espresso")
        
        order1 = joseph.create_order(espresso, 3.5)
        logging.info(f"Order created: Customer={order1.customer.name}, Coffee={order1.coffee.name}, Price={order1.price}")
        
        orders = Order.all_orders()
        logging.info(f"All Orders: {[f'Customer={o.customer.name}, Coffee={o.coffee.name}, Price={o.price}' for o in orders]}")

    except Exception as e:
        logging.error(f"Error: {e}")

    try:
        coffee = Coffee("Espresso")
        customer = Customer("Joseph")
        customer.create_order(coffee, 3.5)
        
        logging.info(f"Coffee Orders: {coffee.orders()}")
        logging.info(f"Coffee Customers: {coffee.customers()}")
        logging.info(f"Coffee Average Price: {coffee.average_price()}")
        logging.info(f"Most Aficionado: {Customer.most_aficionado(coffee.name).name}")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    test_classes()
