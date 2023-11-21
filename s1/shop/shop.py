from typing import List

from .product import Product


class Shop:
    def __init__(self, products: List[Product]):
        self._products = products

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value

    def sort_products_by_price(self):
        return sorted(self._products, key=lambda x: x.cost)

    def get_most_expensive_product(self):
        return max(self._products, key=lambda x: x.cost)
