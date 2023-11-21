from shop.product import Product
from shop.shop import Shop


def test_products_storage():
    # Тест для проверки корректности хранения списка продуктов
    products = [Product(cost=10, title="Товар 1"), Product(cost=5, title="Товар 2")]
    shop = Shop(products)
    assert shop.products == products

def test_most_expensive_product():
    # Тест для проверки корректности метода get_most_expensive_product
    most_expensive_product = Product(cost=15, title="Самый дорогой товар")
    products = [Product(cost=10, title="Товар 1"), Product(cost=5, title="Товар 2"), most_expensive_product]
    shop = Shop(products)
    assert shop.get_most_expensive_product() == most_expensive_product

def test_sort_products_by_price():
    # Тест для проверки корректности метода sort_products_by_price
    products = [Product(cost=10, title="Товар 1"), Product(cost=5, title="Товар 2"), Product(cost=15, title="Товар 3")]
    shop = Shop(products)
    sorted_products = shop.sort_products_by_price()
    assert sorted_products == [products[1], products[0], products[2]]
