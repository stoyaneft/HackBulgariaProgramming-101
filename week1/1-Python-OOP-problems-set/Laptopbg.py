from collections import defaultdict


class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = defaultdict(int)
        self.total_profit = 0

    def load_new_products(self, product, count):
        self.products[product.name] += count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print(product.name + ' - ' + str(product[product.name]))

    def sell_product(self, product):
        self.products[product.name] -= 1
        if self.products[product.name] >= 0:
            self.total_profit += product.profit()
            return True
        return False

    def total_income(self):
        return self.total_profit
