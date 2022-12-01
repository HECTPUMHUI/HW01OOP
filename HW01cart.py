class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product: {self.name}"

    def show_product(self):
        return f'Product is: {self.name} and price is: {self.price}.'

    def total_price(self, quantity):
        return round(self.price * quantity, 2)


class ShoppingCart:

    def __init__(self):
        self.products = []
        self.quantities = []
        self.products_1 = []
        self.quantities_1 = []

    def add_to_cart(self, product: Product, quantity):
        if product not in self.products:
            self.quantities.append(quantity)
            self.products.append(product)
        else:
            if product in self.products:
                index2 = self.products.index(product)
                self.quantities[index2] += quantity

        return self.products, self.quantities

    # test
    # def view_list(self):
    #     for product, quantity in zip(self.products, self.quantities):
    #         result = f'Product: {product} Quantity: {quantity}'
    #     return result

    # worked
    # def add_to_cart(self, product: Product, quantity):
    #     if product in self.products:
    #         self.quantities.append(quantity)
    #         self.products.append(product)
    #     else:
    #         self.products.append(product)
    #         self.quantities.append(quantity)
    #
    #     return self.products, self.quantities

    def total_price(self):
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.total_price(quantity)
        return round(total, 2)


beers = Product('Beers', 15)
mango = Product('Mango', 20)
lemon = Product('Lemon', 111)
kiwi = Product('Kiwi', 15)

cart_1 = ShoppingCart()

cart_1.add_to_cart(beers, 12)
cart_1.add_to_cart(beers, 4)
cart_1.add_to_cart(mango, 4)
cart_1.add_to_cart(mango, 6)
cart_1.add_to_cart(mango, 14)
cart_1.add_to_cart(beers, 3)
cart_1.add_to_cart(lemon, 10)
cart_1.add_to_cart(lemon, 30)
cart_1.add_to_cart(kiwi, 15)
# print(f'view {cart_1.view_list()}')

print(cart_1.products)
print(f'Total product quantity in cart: {sum(cart_1.quantities)}')
print(f'Total price in cart: {cart_1.total_price()}')
#
# print(cart_1.products)
print(cart_1.quantities)
# print(cart_1.view_list())
