"""Тесты для сравнения списков по среднему значению."""

from list_comparer import ListComparer

class TestListComparer:
    """Тесты для класса ListComparer."""

    def test_compare_lists_first_greater(self):
        """Тест, когда у второго списка среднее значение больше."""
        comparer = ListComparer([1, 2, 3], [4, 5, 6])
        result = comparer.compare_lists()
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_lists_second_greater(self):
        """Тест, когда у первого списка среднее значение больше."""
        comparer = ListComparer([4, 5, 6], [1, 2, 3])
        result = comparer.compare_lists()
        assert result == "Первый список имеет большее среднее значение"

    def test_compare_lists_equal(self):
        """Тест, когда средние значения списков равны."""
        comparer = ListComparer([5, 4, 6], [4, 5, 6])
        result = comparer.compare_lists()
        assert result == "Средние значения равны"

    def test_compare_lists_both_empty(self):
        """Тест, когда оба списка пусты."""
        comparer = ListComparer([], [])
        result = comparer.compare_lists()
        assert result == "Средние значения равны"

    def test_compare_lists_first_empty(self):
        """Тест, когда первый список пуст."""
        comparer = ListComparer([], [1, 2, 3])
        result = comparer.compare_lists()
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_lists_second_empty(self):
        """Тест, когда второй список пуст."""
        comparer = ListComparer([1, 2, 3], [])
        result = comparer.compare_lists()
        assert result == "Первый список имеет большее среднее значение"

    def test_calculate_average_non_empty(self):
        """Тест для вычисления среднего значения для непустого списка."""
        comparer = ListComparer([1, 2, 3], [])
        result = comparer.calculate_average([4, 5, 6])
        assert result == 5

    def test_calculate_average_empty(self):
        """Тест для вычисления среднего значения для пустого списка."""
        comparer = ListComparer([], [])
        result = comparer.calculate_average([])
        assert result == 0
