"""Tests the sum fuction int unit.py"""

from lessons.unit import sum

def test_sum_empty() -> None:
    assert sum([]) == 0.0

def test_sum_single_iten() -> None:
    x: list[float] = [110.0]
    assert sum(x) == 110.0

def test_sum_many_items() -> None:
    x: list[float] = [1.0, 2.0, 3.0]
    assert sum(x) == 6.0