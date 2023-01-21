import timeit


def sqrt(n: float) -> float:  # This is the fastest RYO solution, about 40x slower than math.sqrt()
    x0 = 0.0
    x1 = 10.0
    while abs(x1 - x0) > 10 ** -7:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1

def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7) -> float:
    x0 = 0.0
    x1 = guess
    while abs(x1 - x0) > EPSILON:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1

def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7) -> float:
    x0 = 0.0
    x1 = guess
    while (x1 - x0) * (x1 - x0) > EPSILON * EPSILON:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1

def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7, max_iter=1000) -> float:
    x = guess
    for i in range(max_iter):
        x = 0.5 * (x + n / x)
    return x1

def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7, max_iter=1000) -> float:
    x0 = 0.0
    x1 = guess
    for i in range(max_iter):
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
        if abs(x1 - x0) <= EPSILON:
            break
    return x1



N = 10000

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
from numpy import sqrt
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    EPSILON = 10 ** -7

    x0 = 0.0
    x1 = 10.0
    while abs(x1 - x0) > EPSILON:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while abs(x1 - x0) > 10 ** -7:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float) -> float:
    x0 = 0.0
    x1 = 10.0
    while (x1 - x0) * (x1 - x0) > 10 ** -14:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7) -> float:
    x0 = 0.0
    x1 = guess
    while abs(x1 - x0) > EPSILON:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7) -> float:
    x0 = 0.0
    x1 = guess
    while (x1 - x0) * (x1 - x0) > EPSILON * EPSILON:
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7, max_iter=1000) -> float:
    x = guess
    for i in range(max_iter):
        x = 0.5 * (x + n / x)
    return x
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def sqrt(n: float, guess: float=10.0, EPSILON: float=10**-7, max_iter=1000) -> float:
    x0 = 0.0
    x1 = guess
    for i in range(max_iter):
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
        if abs(x1 - x0) <= EPSILON:
            break
    return x1
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))
