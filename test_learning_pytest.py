import pytest
from learning_pytest import add

def test_add():
    assert add(2, 3) == 5


# Example modular tests

# Example Class to be tested
"""
import pytest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero!")
        return x / y
"""

# Example tests
"""class CalculatorTest:
    @pytest.fixture
    def calculator(self):
        from basic_calculator import Calculator
        return Calculator()

    def test_add(self, calculator):
        result = calculator.add(2, 3)
        assert result == 5

    def test_subtract(self, calculator):
        result = calculator.subtract(5, 2)
        assert result == 3

    def test_multiply(self, calculator):
        result = calculator.multiply(4, 3)
        assert result == 12

    def test_divide(self, calculator):
        result = self.calculator.divide(10, 2)
        assert result == 5

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(5, 0)"""