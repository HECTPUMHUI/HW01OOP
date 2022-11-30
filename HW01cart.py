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
            # print(self.products)
            self.quantities.append(quantity)
            self.products.append(product)
            print(self.quantities)
        else:
            if product in self.products:
                res = product
                index2 = self.products.index(res)
                print(f"index {index2}")
                self.quantities[index2] += (quantity + quantity)

        return self.products, self.quantities

    def view_list(self):
        for i in self.products:
            if i in self.products:
                print(self.products)
            else:
                print(self.quantities)

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


beers = Product('Beers', 10)
mango = Product('Mango', 20)
lemon = Product('Lemon', 111)
kiwi = Product('Kiwi', 15)

cart_1 = ShoppingCart()

cart_1.add_to_cart(beers, 1)
cart_1.add_to_cart(beers, 4)
cart_1.add_to_cart(mango, 4)
cart_1.add_to_cart(mango, 6)
cart_1.add_to_cart(beers, 3)
cart_1.add_to_cart(lemon, 10)
cart_1.add_to_cart(lemon, 10)
cart_1.add_to_cart(kiwi, 15)
cart_1.view_list()

# print(cart_1.products)
# print(sum(cart_1.quantities))
# print(cart_1.total_price())
#
print(cart_1.products)
print(cart_1.quantities)
