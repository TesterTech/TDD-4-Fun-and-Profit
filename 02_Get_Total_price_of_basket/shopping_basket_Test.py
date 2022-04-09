import unittest
from shopping_basket import ShoppingBasket


class TestBasket(unittest.TestCase):

    def test_item_can_be_added_to_the_basket(self):
        basket_instance = ShoppingBasket()
        basket_instance.add()
        basket_instance.add()
        self.assertEqual(2, basket_instance.size)

    def test_get_total_price_of_items_in_basket(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(10.0)
        basket_instance.add(11.0)
        self.assertEqual(21.0, basket_instance.total_price)



if __name__ == "__main__":
    unittest.main()
