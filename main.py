#2-masala
class Car:
    def __init__(self, model, price):
        self.model = model
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

c1 = Car("Malibu", 30000)

print(c1.price)

c1.price = 35000
print(c1.price)
