import pytest

from src.calculator import add, average, divide, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_average():
    assert average([1, 2, 3, 4]) == 2.5


def test_average_empty():
    with pytest.raises(ValueError):
        average([])


def test_power():
    assert power(2, 3) == 8
