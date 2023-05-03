# Agregation is one way more specialized od association
# between two or more objects. Each object will have its
# life cicle splited.
# Usualy is a relationship of one to many, where one
# object has one or many objects.
# The objects can life apart, but it can be treated as
# a relation where the object need another one to do
# a task.
# There a controversies about the agregation definition.

class Cart:
    def __init__(self):
        self._product = []
    

    def total(self):
        return sum([p.price for p in self._product])
    

    def list_product(self):
        for product in self._product:
            print(product.name, product.price)
    

    def insert_products(self, *product_class):
        for i in product_class:
            self._product.append(i)


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


cart_01 = Cart()
p1, p2 = Product('beans', 10.99), Product('Juice', 2.99)

cart_01.insert_products(p1, p2)
cart_01.list_product()
print(cart_01.total())
