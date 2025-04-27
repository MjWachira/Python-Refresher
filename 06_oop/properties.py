# Properties
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

item = Product(50)
print(item.price)
