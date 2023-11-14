
from datetime import date

class Client:
    client_id = 0

    def __init__(self , last_name, first_name):
        self.id = Client.client_id
        Client.client_id += 1
        self.last_name = last_name
        self.first_name = first_name

class Product:
    def __init__(self , name , price):
        self.name = name
        self.price = price

class Transaction:
    def __init__(self , client , product , date):
        self.client = client
        self.product = product
        self.date = date

class Store:
    products = [

    ]

    transactions = []

    @classmethod #?????????
    def sell_product(cls , client_id, product_name, transaction_date):
        found_client = None
        for transaction in cls.transactions:
            if transaction.client.id == client_id:
                found_client = transaction.client
                break

        if found_client is None:
            found_client = Client("Unknown", "Client")

        found_product = None
        for product in cls.products:
            if product.name == product_name:
                found_product = product
                break

        if found_product is not None:
            transaction = Transaction(found_client, found_product, transaction_date)
            cls.transactions.append(transaction)
            print(f"Sold {found_product.name} to {found_client.first_name} {found_client.last_name} on {transaction_date}.")


Store.products = [
    Product("Product 1", 10.0),
    Product("Product 2", 20.0),
    Product("Product 3", 15.0),
    Product("Product 4", 25.0),
    Product("Product 5", 30.0)
]

Store.sell_product(1, "Product 1", date(2023, 11, 8))
Store.sell_product(2, "Product 2", date(2023, 11, 8))
Store.sell_product(1, "Product 3", date(2023, 11, 9))
Store.sell_product(3, "Product 4", date(2023, 11, 10))