import pytest
from calculator import Calculator


class TestCalculator:
    # Тестування додавання
    def test_add_integers(self):
        assert Calculator.add(2, 3) == 5

    def test_add_invalid_input_type(self):
        with pytest.raises(TypeError) as excinfo:
            Calculator.add("2", 3)
        assert "Obydva arhumenty povynni buty chyslamy" in str(excinfo.value)

        with pytest.raises(TypeError):
            Calculator.add(2, "3")

    # Тестування віднімання
    def test_subtract_integers(self):
        assert Calculator.subtract(5, 3) == 2

    def test_subtract_invalid_input_type(self):
        with pytest.raises(TypeError) as excinfo:
            Calculator.subtract("5", 3)
        assert "Obydva arhumenty povynni buty chyslamy" in str(excinfo.value)

    # Тестування множення
    def test_multiply_integers(self):
        assert Calculator.multiply(2, 3) == 6

    def test_multiply_invalid_input_type(self):
        with pytest.raises(TypeError) as excinfo:
            Calculator.multiply("2", 3)
        assert "Obydva arhumenty povynni buty chyslamy" in str(excinfo.value)

    # Тестування ділення
    def test_divide_integers(self):
        assert Calculator.divide(6, 2) == 3

    def test_divide_by_zero(self):
        with pytest.raises(ValueError) as excinfo:
            Calculator.divide(6, 0)
        assert "Dilennya na nul" in str(excinfo.value)
        assert "nemozhlyve" in str(excinfo.value)

    def test_divide_invalid_input_type(self):
        with pytest.raises(TypeError) as excinfo:
            Calculator.divide("6", 2)
        assert "Obydva arhumenty povynni buty chyslamy" in str(excinfo.value)

    # Тестування методу calculate
    @pytest.mark.parametrize("a,b,op,expected", [
        (10, 5, '+', 15),
        (10, 5, '-', 5),
        (10, 5, '*', 50),
        (10, 5, '/', 2),
    ])
    def test_calculate_operations(self, a, b, op, expected):
        assert Calculator.calculate(a, b, op) == expected

    def test_calculate_invalid_operation(self):
        with pytest.raises(ValueError):
            Calculator.calculate(2, 3, '%')