import timeit


def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while (x1 - x0 < -10 ** -8) or (x1 - x0 > 10 ** -8):  # slightly faster than using abs()
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1


N = 100000

stmt = """
sqrt(0)
sqrt(123_456_789)
sqrt(123_456_789_123_456)
"""

setup = """
from math import sqrt
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while abs(x1 - x0) > 10 ** -8:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while not (-10 ** -8 < x1 - x0 < 10 ** -8):
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while (x1 - x0 < -10 ** -8) or (x1 - x0 > 10 ** -8):
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while (x1 - x0 <= -10 ** -8) or (x1 - x0 >= 10 ** -8):
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))