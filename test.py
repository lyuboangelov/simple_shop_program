import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)
plt.show()

prod = {'banan': {'quantity': 10, 'price': 10, 'barcode': 10}}

print(prod)

class Product():

    def __init__(self, name, quantity, price, barcode):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.barcode = barcode

    def change_price(self, new_price):
        self.price = new_price
        return self.price


apple = Product('apple', 2, 3, 5)

print(apple.name, apple.quantity)
apple.quantity += 4
print(apple.quantity)
apple.change_price(99)
print(apple.price)


banan = Product('banan', prod['banan']['quantity'], prod['banan']['price'], prod['banan']['barcode'])
print(banan.quantity, banan.name)