import pytest
from string_utils import StringUtils


# Создаем объект один раз для всех тестов
@pytest.fixture
def utils():
    return StringUtils()


#  CAPITALIZE
class TestCapitalize:
    """Тесты для метода capitalize"""

    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [
        ("word", "Word"),
        ("new work", "New work"),
        ("python", "Python"),
        ("слово", "Слово"),  # русские буквы
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        """Позитивные тесты: обычные строки"""
        assert utils.capitalize(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, expected", [
        ("", ""),                # пустая строка
        ("   ", "   "),          # только пробелы
        ("123", "123"),          # цифры
        ("@word", "@word"),      # спецсимвол в начале
        (" python", " python"),  # пробел в начале (баг!)
    ])
    def test_capitalize_negative(self, utils, input_str, expected):
        """Негативные тесты: краевые случаи"""
        assert utils.capitalize(input_str) == expected

    @pytest.mark.bug
    def test_capitalize_bug(self, utils):
        """Тесты, которые выявляют баги"""
        # Этот тест должен упасть - это нормально!
        assert utils.capitalize(" python") == " Python"  # баг


#  TRIM
class TestTrim:
    """Тесты для метода trim"""

    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [
        ("   word", "word"),        # пробелы в начале
        ("  python  ", "python  "),  # пробелы в начале и конце
        (" new work", "new work"),  # пробелы в начале и середине
        ("\t\n word", "\t\n word"),  # табуляции не удаляются (баг)
    ])
    def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, expected", [
        ("", ""),               # пустая строка
        ("skypro", "skypro"),   # строка без пробела
        ("   ", ""),            # только пробелы
    ])
    def test_trim_negative(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected


# CONTAINS
class TestContains:
    """Тесты для метода contains"""

    @pytest.mark.positive
    @pytest.mark.parametrize("string, symbol, expected", [
        ("Word", "W", True),       # символ с верхним регистром
        ("python", "o", True),     # символ с нижним регистром
        ("new work", " ", True),   # пробел тоже символ
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("string, symbol, expected", [
        ("Word", "D", False),    # символ с верхним регистром
        ("", "a", False),        # пустая строка
        ("Python", "p", False),  # символ с нижним регистром
        ("word", "", True),      # пустой символ
        ("", "", True)           # пустой символ и строка
    ])
    def test_contains_negative(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected


# DELETE_SYMBOL
class TestDeleteSymbol:
    """Тесты для метода delete_symbol"""

    @pytest.mark.positive
    @pytest.mark.parametrize("string, symbol, expected", [
        ("Word", "r", "Wod"),            # один символ
        ("banana", "a", "bnn"),          # несколько символов
        ("New work", " ", "Newwork"),    # пробел
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("string, symbol, expected", [
        ("Word", "X", "Word"),     # символ не найден
        ("", "a", ""),             # пустая строка
        ("python", "", "python"),  # пустой символ
    ])
    def test_delete_symbol_negative(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected
