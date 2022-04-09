class ShoppingBasket:

    def __init__(self):
        self.size = 0
        self.basket_list = []
        self.total_price = 0

    def add(self, price=0):
        if price >= 0:
            self.basket_list.append(price)
            self.total_price = self.total_price + price
        self.size = len(self.basket_list)
