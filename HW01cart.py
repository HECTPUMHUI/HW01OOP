"""
Constructors
1)Implement both Product and ShoppingCart initializers to provide required data
while creating instances.
It's ok to initialize empty carts.
1) можна створити пустий об'єкт для роботи з двома кошиками(двома різними об'єктами)
2) Implement a human readable string representations for these classes.
2) додати __стр__ для відображення об'єктів класу
3) Apple (Fruit) equals to Apple (MacBook)?
Implement equality comparison for the Product instances. Consider the products are
equal in case both objects
have the same name and price.
3)умова для порівнняня, об'єкти різні при однакових іменах, якщо їх ціна різна
Casting
4) Implement type-casting for Product and ShoppingCart. - Product cast to float type
 should be equal to its price -
Product cast to string type should be equal to its name - ShoppingCart cast to float
type should be equal to
 its total price
4) переклад розумію, суть не дуже)
Refactor products
5) Refactor add_product method in a way to avoid product instances duplication in the cart -
adjust appropriate quantities only.
5) переробити метод, якщо продукти дублюються, змінювати тільки кількість
Addition
6)Implement addition behavior for ShoppingCart class: - if a Product is added to the cart,
 the behavior is the same as for add_product method with quantity = 1. - if another
 ShoppingCart instance is
 added the result is an instance of the same type containing products and their
 quantities from both carts
6) тут пояснення поведінки методу у класі Кошика при додаванні продукти в кошик.

"""


class Product:

    def __init__(self, name, price):
        """Object constructor"""
        self.name = name
        self.price = price

    def __repr__(self):
        """Help for view"""
        return f"Product: {self.name}"

    def show_product(self):
        return f'Product is: {self.name} and price is: {self.price}.'

    def total_price(self, quantity):
        return round(self.price * quantity, 2)


class ShoppingCart:

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
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.total_price(quantity)
        return f'Total: {round(total, 2)}'


beers = Product('Beers', 15)
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
cart_2.add_to_cart(mango, 35)
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


cart_total = cart_1.__add__(cart_2)
print(cart_total)
# print(isinstance(cart_1, ShoppingCart))
print(cart_total.total_price())
