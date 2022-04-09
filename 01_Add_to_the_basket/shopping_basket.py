class ShoppingBasket:

    def __init__(self):
        self.size = 0
        self.basket_list = []
        self.total_price = 0

    def add(self):
        self.basket_list.append(self)
        self.size = self.basket_list.count(self)
