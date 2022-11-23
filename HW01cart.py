"""
Challenge:
#. Implement ``Product`` class
Each ``Product`` instance should implement properties:
    * ``name`` - a product's name, like apple, cheese etc.
    * ``price`` - a price for a single unit
#. ``Product`` instance should have a behavior of calculating total
   price for a specified quantity of goods
Implement ``ShoppingCart`` class
#. ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
#. ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.

"""


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}"

    def show_product(self):
        return f'product is: {self.name} and price is: {self.price}.'

    def total_price(self, quantity):
        return f'total price will: {self.price * quantity}, if quantity {quantity}.'


beers = Product('Beers', 100)
mango = Product('Mango', 70)

print(beers.show_product())
print(beers.total_price(14))
print(mango.show_product())
print(mango.total_price(8))


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_to_cart(self, product: Product, quantity):
        self.products.append(product)
        self.quantities.append(quantity)
        for i in range(len(self.products)):
            print(self.products[i])
        for i in range(len(self.quantities)):
            print(f'quantities: {self.quantities[i]}')

    def total_price(self):
        pass


cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_to_cart(beers, 5)
cart_2.add_to_cart(mango, 6)
