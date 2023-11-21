from calculator.test import test_calculating_discount, test_calculator, test_square_root_extraction
from shop.test import test_most_expensive_product, test_products_storage, test_sort_products_by_price


test_calculator()
test_square_root_extraction()
test_calculating_discount()
print("Тесты калькулятора пройдены!")

test_products_storage()
test_most_expensive_product()
test_sort_products_by_price()
print("Тесты магазина пройдены!")
