import unittest
from shopping_basket import ShoppingBasket
from product import Product, Video, Book


class TestBasket(unittest.TestCase):

    def test_item_can_be_added_to_the_basket(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(Product(0))
        basket_instance.add(Product(10))
        basket_instance.add(Product(0))
        basket_instance.add(Product(0))
        self.assertEqual(4, basket_instance.get_size())

    def test_get_total_price_of_items_in_basket(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(Product(10.0))
        basket_instance.add(Product(11.0))
        self.assertEqual(21.0, basket_instance.get_total_price())

    def test_cannot_add_with_negative_price(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(Product(10.0))
        basket_instance.add(Product(-10.0))
        basket_instance.add(Product(-1.0))
        self.assertEqual(1, basket_instance.get_size())

    def test_add_sales_tax_to_total(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(Product(10.0))
        basket_instance.add(Product(10.0))
        self.assertEqual(24.0, basket_instance.get_total_price_with_sales_tax())

    def test_can_add_different_products_to_the_basket(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(Book(22.0))
        basket_instance.add(Video(10.0))
        self.assertAlmostEqual(32, basket_instance.get_total_price())


if __name__ == "__main__":
    unittest.main()
