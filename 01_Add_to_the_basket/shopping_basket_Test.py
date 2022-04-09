import unittest
from shopping_basket import ShoppingBasket


class TestBasket(unittest.TestCase):

    def test_item_can_be_added_to_the_basket(self):
        basket_instance = ShoppingBasket()
        basket_instance.add(self)
        basket_instance.add(self)
        self.assertEqual(2, basket_instance.size)


if __name__ == "__main__":
    unittest.main()
