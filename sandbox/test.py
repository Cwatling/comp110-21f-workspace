"""List utility functions."""

__author__ = "730412366"


def all(xs: list[int], test: int) -> bool:
    """Tests if all the items in the list are the same as the inputed test int"""
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
        
print(all([1, 1, 1], 1))
