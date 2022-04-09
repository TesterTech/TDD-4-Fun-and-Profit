class ShoppingBasket:

    def __init__(self):
        self._total_price = 0
        self._size = 0
        self._basket_list = []

    def add(self, product=None):
        price = product.get_price()
        if price >= 0:
            self._basket_list.append(type(product)(price))

    def get_total_price(self) -> int:
        total_price = sum(product_item.get_price() for product_item in self._basket_list)
        return total_price

    def get_total_price_with_sales_tax(self, sales_tax: float = None) -> float:
        if sales_tax is not None:
            sales_tax_multiplier = sales_tax
        else:
            sales_tax_multiplier = 1.20
        intermediary_price = sum(product_item.get_price() for product_item in self._basket_list)
        return intermediary_price * sales_tax_multiplier

    def get_size(self) -> int:
        return len(self._basket_list)
