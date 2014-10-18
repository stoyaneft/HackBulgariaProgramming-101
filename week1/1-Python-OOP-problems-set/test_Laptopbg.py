import unittest

from Laptopbg import Product, Laptop, Smartphone, Store


class LaptopBgTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_product_initialization(self):
        new_product = Product('Dell Inspiron', 1000, 1350)
        self.assertEqual(new_product.name, 'Dell Inspiron')
        self.assertEqual(new_product.stock_price, 1000)
        self.assertEqual(new_product.final_price, 1350)

    def test_product_profit(self):
        new_product = Product('Dell Inspiron', 1000, 1350)
        self.assertEqual(new_product.profit(), 350)

    def test_load_new_products_in_store(self):
        new_store = Store('Laptop.bg')
        new_laptop = Laptop('Dell Inspiron', 1000, 1350, 6, 512)
        new_store.load_new_products(new_laptop, 10)
        self.assertEqual(new_store.products['Dell Inspiron'], 10)
        new_store.load_new_products(new_laptop, 10)
        self.assertEqual(new_store.products['Dell Inspiron'], 20)

    def test_sell_product(self):
        store = Store('Laptop.bg')
        smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        store.load_new_products(smarthphone, 2)
        self.assertTrue(store.sell_product(smarthphone))
        self.assertTrue(store.sell_product(smarthphone))
        self.assertFalse(store.sell_product(smarthphone))

    def test_total_income(self):
        store = Store('Laptop.bg')
        smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        store.load_new_products(smarthphone, 2)
        store.sell_product(smarthphone)
        store.sell_product(smarthphone)
        self.assertEqual(store.total_income(), 640)

if __name__ == '__main__':
    unittest.main()
