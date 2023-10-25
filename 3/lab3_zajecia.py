
class Product:
    def __init__(self , name , quantity , price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
                return f"Produkt: {self.name}\nIlość: {self.quantity}\nCena: {self.price}\n"

class Client:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
    
    # def buy(se)


products = [
    Product("Komputer" , 7 , 2000),
    Product("Laptop" , 15 , 5000)
] 

clients = [
    Client("Jan Kowalski" , 19000),
    Client("Anna Nowak" , 800)
]           

#Wypisanie informacji o elementach listy obiektów Product

list_of_products_in_warehouse = [product.name for product in products]

print(list_of_products_in_warehouse)

#Wypisanie informacji o obiekcie Product

product1 = products[0]
product2 = products[1]

print(product1)
print(product2)

#Wypisanie informacji o elementach listy obiektów Client

list_of_clients = [client.name for client in clients]

print(list_of_clients)

#