class OrderedStatus:
    def __init__(self):
        self.hasShipped = False


class Order:
    def __init__(self):
        self.productOrdered = []
        self.status = OrderedStatus()


class Product:
    def __init__(self, id, price):
        self.productID = id
        self.productPrice = price


product1 = Product("beans", 0.45)
product2 = Product("eggs", 1.25)

myOrder = Order()
myOrder.productOrdered.append(product1)
myOrder.productOrdered.append(product2)

print(myOrder.status.hasShipped)
print(myOrder.productOrdered[0].productID)
print(myOrder.productOrdered[0].productPrice)

print(myOrder.productOrdered[1].productID)
print(myOrder.productOrdered[1].productPrice)
