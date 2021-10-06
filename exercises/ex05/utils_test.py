"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730412366"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub

"""Tests for only even function."""


def test_only_evens_empty_list() -> None:
    """Tests when the input is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_zero() -> None:
    """Tests when the input is zero."""
    xs: list[int] = [0]
    assert only_evens(xs) == [0]


def test_only_evens_use() -> None:
    """Tests for standard use case."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


"""Test for concat function."""


def test_concat_empty_lists() -> None:
    """Test for when both lists are empty."""
    xs: list[int] = []
    xy: list[int] = []
    assert concat(xs, xy) == []


def test_concat_empty_list_first() -> None:
    """Tests for when the first input is an empty list."""
    xs: list[int] = []
    xy: list[int] = [4, 5, 6]
    assert concat(xs, xy) == [4, 5, 6]


def test_concat_use() -> None:
    """Tests for standard use case."""
    xs: list[int] = [1, 2, 3]
    xy: list[int] = [4, 5, 6]
    assert concat(xs, xy) == [1, 2, 3, 4, 5, 6]


"""Tests for sub function."""


def test_sub_negative_start() -> None:
    """Tests when the start index is negative."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = -5
    end: int = 5
    assert sub(xs, start, end) == [1, 2, 3, 4, 5]


def test_sub_out_of_range_end() -> None:
    """Tests when the end index it out of the range of the list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 3
    end: int = 10
    assert sub(xs, start, end) == [4, 5, 6]


def test_sub_use() -> None:
    """Tests the standard use case."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 2
    end: int = 5
    assert sub(xs, start, end) == [3, 4, 5]
