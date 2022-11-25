class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}"

    def show_product(self):
        return f'product is: {self.name} and price is: {self.price}.'

    def total_price(self, quantity):
        return round(self.price * quantity, 2)


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_to_cart(self, product: Product, quantity):
        self.products.append(product)
        self.quantities.append(quantity)
        return self.products, self.quantities

    def total_price(self):
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.total_price(quantity)
        return round(total, 2)


beers = Product('Beers', 10.59)
mango = Product('Mango', 36.55)

cart_1 = ShoppingCart()

cart_1.add_to_cart(beers, 0.7)
cart_1.add_to_cart(mango, 4)

print(cart_1.total_price())
