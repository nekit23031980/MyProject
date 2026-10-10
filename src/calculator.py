"""Прості арифметичні та статистичні функції для демонстрації CI/CD."""

from typing import Iterable


def add(a: float, b: float) -> float:
    """Повертає суму двох чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Повертає різницю двох чисел."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Повертає добуток двох чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Повертає частку; при діленні на нуль піднімає ValueError."""
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


def average(values: Iterable[float]) -> float:
    """Повертає середнє арифметичне; для порожньої послідовності - ValueError."""
    data = list(values)
    if not data:
        raise ValueError("Порожня послідовність")
    return sum(data) / len(data)


def power(a: float, b: float) -> float:
    """Повертає a у степені b."""
    return a**b
