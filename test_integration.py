import pytest
from calculator import Calculator


class TestIntegration:
    def test_full_operation_chain(self):
        result = Calculator.add(2, 3)
        assert result == 5

        result = Calculator.multiply(result, 4)
        assert result == 20

        result = Calculator.subtract(result, 5)
        assert result == 15

        result = Calculator.divide(result, 3)
        assert result == 5

    def test_error_handling_flow(self):
        with pytest.raises(ValueError) as excinfo:
            Calculator.divide(5, 0)
        assert "Dilennya na nul" in str(excinfo.value)
        assert "nemozhlyve" in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            Calculator.add("invalid", 5)
        assert "Obydva arhumenty povynni buty chyslamy" in str(excinfo.value)