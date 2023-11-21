from .calculator import Calculator
import pytest


def test_calculator():
    assert Calculator.calculation(2, 6, '+') == 8
    assert Calculator.calculation(2, 2, '-') == 0
    assert Calculator.calculation(2, 7, '*') == 14
    assert Calculator.calculation(100, 50, '/') == 2

    # Тестирование исключения при делении на ноль
    with pytest.raises(ArithmeticError, match="Division by zero is not possible"):
        Calculator.calculation(8, 0, '/')

def test_square_root_extraction():
    assert Calculator.square_root_extraction(169) == 13
    assert Calculator.square_root_extraction(25) == 5
    assert Calculator.square_root_extraction(0) == 0
    # Тестирование исключения при попытке извлечения корня из отрицательного числа
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        Calculator.square_root_extraction(-1)

    # Тестирование исключения при попытке извлечения корня из бесконечности
    with pytest.raises(ValueError, match="Cannot calculate square root of infinity"):
        Calculator.square_root_extraction(float('inf'))

    # Тестирование исключения при попытке извлечения корня из NaN
    with pytest.raises(ValueError, match="Cannot calculate square root of NaN"):
        Calculator.square_root_extraction(float('nan'))

def test_calculating_discount():
    assert Calculator.calculating_discount(100, 10) == 90
    assert Calculator.calculating_discount(200, 25) == 150
