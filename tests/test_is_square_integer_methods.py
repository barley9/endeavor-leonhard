import timeit
# import math


N = 100

setup = """
from math import sqrt, floor

EPSILON = 10 ** -7

def is_square_int(n: int) -> bool:
    sqrtn = sqrt(n)
    return sqrtn - int(sqrtn) < EPSILON

def is_square_floor(n: int) -> bool:
    sqrtn = sqrt(n)
    return sqrtn - floor(sqrtn) < EPSILON  # uses math.floor()

def is_square_search(n: int) -> bool:
    # locate upper bound for i
    high = 10_000
    while high * high < n:
        high *= high

    # binary search for integer which squares to equal n
    low = 0
    while high - low > 1:
        mid = low + (high - low) // 2
        mid2 = mid * mid
        if mid2 == n:
            return True
        elif mid2 < n:
            low = mid
        else:
            high = mid
    return False
"""

stmt = """
for i in range(100, 100_000):
    is_square_int(i)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

stmt = """
for i in range(100, 100_000):
    is_square_floor(i)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

stmt = """
for i in range(100, 100_000):
    is_square_search(i)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))