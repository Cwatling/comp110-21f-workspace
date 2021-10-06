"""List utility functions part 2."""

__author__ = "730412366"


def only_evens(xs: list[int]) -> list[int]:
    """Returns the even numbers in a list."""
    output: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            output.append(xs[i])
        i += 1
    return output


def concat(xs: list[int], xy: list[int]) -> list[int]:
    """Combines two strings."""
    output: list[int] = xs + xy
    return output


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns a string of the points inbetween the indexs."""
    x: int = start
    y: int = end
    output: list[int] = []
    if x < 0:
        x = 0
    elif y > len(xs):
        y = len(xs)
        
    while x < y:
        output.append(xs[x])
        x += 1
    return output
