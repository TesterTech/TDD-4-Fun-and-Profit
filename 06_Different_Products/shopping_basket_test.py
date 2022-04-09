import unittest
from shopping_basket import ShoppingBasket
from product import Product, Video, Book


class TestBasket(unittest.TestCase):

    basket_instance = None

    def setUp(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(Product())
        basket_instance.add(Product())
        self.basket_instance = basket_instance

    def test_item_can_be_added_to_the_basket(self):
        self.assertEqual(2, self.basket_instance.get_size())

    def test_get_total_price_of_items_in_the_basket(self):
        self.basket_instance.add(Product(10.0))
        self.basket_instance.add(Product(11.0))
        self.assertEqual(21.0, self.basket_instance.get_total_price())

    def test_cannot_add_with_negative_price(self):
        self.basket_instance.add(Product(-10.0))
        self.assertEqual(2, self.basket_instance.get_size())

    def test_add_sales_tax_to_total(self):
        self.basket_instance.add(Product(5.0))
        self.basket_instance.add(Product(5.0))
        self.assertEqual(12, self.basket_instance.get_total_price_with_sales_tax())

    def test_add_arbitrary_sales_tax_to_total(self):
        self.basket_instance.add(Product(5.0))
        self.basket_instance.add(Product(5.0))
        self.assertEqual(11, self.basket_instance.get_total_price_with_sales_tax(1.10))

    def test_add_different_products_to_the_basket(self):
        self.basket_instance.add(Video(5.0))
        self.basket_instance.add(Book(5.0))
        self.assertEqual(10, self.basket_instance.get_total_price())




if __name__ == '__main__':
    unittest.main()
