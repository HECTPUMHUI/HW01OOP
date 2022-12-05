"""
    This script emulate the behavior of Shop and Bye something.

"""


class Product:
    """Create a new Product"""

    def __init__(self, name, price):
        """Object constructor"""
        self.name = name
        self.price = price

    def __repr__(self):
        """Help for view"""
        return f"Product: {self.name}"

    def show_product(self):
        """Show the product"""
        return f'Product is: {self.name} and price is: {self.price}.'

    def total_price(self, quantity):
        """Total price"""
        return round(self.price * quantity, 2)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price


class ShoppingCart:
    """Shopping Cart"""

    def __init__(self):
        """Object constructor"""
        self.products = []
        self.quantities = []

    def add_to_cart(self, product: Product, quantity):
        """Add to cart product and calculate quantity"""
        if product not in self.products:
            self.quantities.append(quantity)
            self.products.append(product)
        else:
            if product in self.products:
                index2 = self.products.index(product)
                self.quantities[index2] += quantity

        return self.products, self.quantities

    def __add__(self, other):
        """peregruzka magic method for calculating items in two carts"""
        if isinstance(other, Product):
            self.add_to_cart(other, 1)
            return self

        if isinstance(other, ShoppingCart):
            cart = ShoppingCart()
            for product, quantity in zip(self.products + other.products,
                                         self.quantities + other.quantities):
                cart.add_to_cart(product, quantity)
            return cart

    def __repr__(self):
        return f'Add: {self.products} \n' \
               f'Quantities: {self.quantities}'

    def total_price(self):
        """Returns the total price"""
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.total_price(quantity)
        return f'Total: {round(total, 2)}'


beers = Product('Beers', 15)
beers_1 = Product('Beers', 100)
mango = Product('Mango', 20)
lemon = Product('Lemon', 11)
kiwi = Product('Kiwi', 15)

cart_total = ShoppingCart()
cart_1 = ShoppingCart()
cart_2 = ShoppingCart()

cart_1.add_to_cart(beers, 12)
cart_1.add_to_cart(beers, 4)
# cart_1.add_to_cart(mango, 4)
# cart_1.add_to_cart(mango, 6)
# cart_1.add_to_cart(mango, 15)
cart_1.add_to_cart(beers, 4)
cart_1.add_to_cart(lemon, 10)
cart_1.add_to_cart(lemon, 30)
cart_1.add_to_cart(mango, 35)
cart_1.add_to_cart(kiwi, 15)

cart_2.add_to_cart(mango, 35)
cart_2.add_to_cart(beers_1, 35)
cart_2.add_to_cart(beers_1, 10)
cart_2.add_to_cart(mango, 35)
cart_2.add_to_cart(beers, 15)
cart_2.add_to_cart(beers, 15)

# print(cart_1.products)
# print(cart_2.products)
#
# print(f'Total product quantity in cart: {sum(cart_1.quantities)}')
# print(f'Total price in cart: {cart_1.total_price()}')
# print(f'Total product quantity in cart: {sum(cart_2.quantities)}')
# print(f'Total price in cart: {cart_2.total_price()}')
#
# print(cart_1.quantities)
# cart_total.cart_to_cart(cart_1, cart_2)
# print(cart_1)
# print(cart_2)


# cart_total = cart_1.__add__(cart_2)
cart_total = cart_1 + cart_2
print(cart_total)
# print(isinstance(cart_1, ShoppingCart))
print(cart_total.total_price())
