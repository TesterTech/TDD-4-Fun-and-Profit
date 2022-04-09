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

    def get_total_price(self) -> int:
        total_price = self.total_price
        return total_price

    def get_total_price_with_sales_tax(self) -> float:
        sales_tax_multiplier = 1.20
        total_price = self.total_price
        return total_price * sales_tax_multiplier

