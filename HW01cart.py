"""
Challenge:

#. Implement ``Product`` class
#. Each ``Product`` instance should implement properties:
    * ``name`` - a product's name, like apple, cheese etc.
    * ``price`` - a price for a single unit
#. ``Product`` instance should have a behavior of calculating total
   price for a specified quantity of goods
#. Implement ``ShoppingCart`` class
#. ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
#. ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.

"""


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        return f'product is: {self.name} and price is: {self.price}.'

    def total_price(self, quantity):
        return f'total price will: {self.price * quantity}.'


beers = Product('Beers', 100)
mango = Product('Mango', 70)

print(beers.show_product())
print(beers.total_price(14))
print(mango.total_price(3))


class ShoppingCart:
    dict_cart = {}

    def add_to_cart(self, product: Product, quantity):
        self.dict_cart = product
        print(self.dict_cart) # check

    def total_price(self):
        pass


cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_to_cart(beers, 5)
cart_2.add_to_cart(mango, 5)
