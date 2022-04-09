class ShoppingBasket:

    size = var = 0
    basket_list = var = []

    def add(self):
        ShoppingBasket.basket_list.append(self)
        ShoppingBasket.size = ShoppingBasket.basket_list.count(self)
