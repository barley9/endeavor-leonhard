"""
figurate.py

This module contains useful functions for working with figurate (aka polygonal) numbers
"""

import math


#### Functions to compute figurate numbers ####

def triangle(n: int) -> int:
    """Returns the nth triangular number"""
    return (n * (n + 1)) // 2

def square(n: int) -> int:
    """Returns the nth square number"""
    return n * n

def pentagon(n: int) -> int:
    """Returns the nth pentagonal number"""
    return n * (3 * n - 1) // 2

def hexagon(n: int) -> int:
    """Returns the nth hexagonal number"""
    return n * (2 * n - 1)

def heptagon(n: int) -> int:
    """Returns the nth heptagonal number"""
    return n * (5 * n - 3) // 2

def octagon(n: int) -> int:
    """Returns the nth octagonal number"""
    return n * (3 * n - 2)

def figurate(p: int, n: int) -> int:
    if p == 3:
        return triangle(n)
    elif p == 4:
        return square(n)
    elif p == 5:
        return pentagon(n)
    elif p == 6:
        return hexagon(n)
    elif p == 7:
        return heptagon(n)
    elif p == 8:
        return octagon(n)
    else:
        raise NotImplementedError


#### Inverses of above functions ####

def inverse_triangle(i: int) -> float:
    return math.sqrt((2 * i) + (1/4)) - (1/2)

def inverse_square(i: int) -> float:
    return math.sqrt(i)

def inverse_pentagon(i: int) -> float:
    return math.sqrt(((2 * i) + (1/12)) / 3) + (1/6)

def inverse_hexagon(i: int) -> float:
    return math.sqrt((i + (1/8)) / 2) + (1/4)

def inverse_heptagon(i: int) -> float:
    return math.sqrt(((2 * i) + (9/20)) / 5) + (3/10)

def inverse_octagon(i: int) -> float:
    return math.sqrt((i + (1/3)) / 3) + (1/3)

def inverse_figurate(p: int, i: int) -> float:
    if p == 3:
        return inverse_triangle(i)
    elif p == 4:
        return inverse_square(i)
    elif p == 5:
        return inverse_pentagon(i)
    elif p == 6:
        return inverse_hexagon(i)
    elif p == 7:
        return inverse_heptagon(i)
    elif p == 8:
        return inverse_octagon(i)
    else:
        raise NotImplementedError