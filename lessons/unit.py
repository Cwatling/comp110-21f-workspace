"""Messing with unit functions"""

def sum(x: list[float]) -> float:
    i: int = 0
    total: float = 0.0
    while i < len(x):
        total += x[i]
        i += 1

    return total