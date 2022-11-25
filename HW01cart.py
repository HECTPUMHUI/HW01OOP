
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
        self.list_1 = []
        self.total = 0

    def add_to_cart(self, product: Product, quantity):
        self.products.append(product)
        self.quantities.append(quantity)
        return self.products, self.quantities
        # for i in range(len(self.products)):
        #     print(f'prod list: {self.products[i]}')
        # for i in range(len(self.quantities)):
        #     print(f'quantities: {self.quantities[i]}')

    def total_price(self):
        for i in range(len(self.products)):
            print(self.products[i].price)
            self.total = self.products[i].price * self.quantities[i]
        print(f'T: {self.total}')

        self.list_1.append(self.total)
        print(f'In cart is {len(self.products)} items.')
        return self.list_1


cart_1 = ShoppingCart()
cart_2 = ShoppingCart()
cart_1.add_to_cart(beers, 1)
cart_2.add_to_cart(mango, 24)
print(cart_1.total_price())
print(cart_2.total_price())

