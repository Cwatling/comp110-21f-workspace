"""List utility functions."""

__author__ = "730412366"


def all(xs: list[int], test: int) -> bool:
    """Tests if all the items in the list are the same as the inputed test int."""
    i: int = 0
    check: int = test
    if len(xs) == 0:
        return False
    else:
        while i < len(xs):
            if check != xs[i]:
                return False
            i += 1
        return True


def max(xs: list[int]) -> int:
    """Find the biggest int in a list."""
    if len(xs) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        max: int = xs[0]
        i: int = 1
        while i < len(xs):
            if max < xs[i]:
                max = xs[i]
            i += 1
        return max


def is_equal(xs: list[int], xy: list[int]) -> bool:
    """Chekcs if two lists are equal to eachother."""
    if len(xs) == len(xy):
        i: int = 0
        while i < len(xs):
            if xs[i] == xy[i]:
                i += 1
            else:
                return False
    else:
        return False
    return True