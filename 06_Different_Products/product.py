class Product:
    def __init__(self, price=0):
        self._price = price

    def get_price(self) -> float:
        return self._price


class Book:
    def __init__(self, price=0):
        self._price = price

    def get_price(self) -> float:
        return self._price


class Video:
    def __init__(self, price=0):
        self._price = price

    def get_price(self) -> float:
        return self._price