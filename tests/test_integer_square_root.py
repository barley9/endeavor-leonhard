import timeit


def integer_sqrt(n: int) -> int:
    low = 0
    high = 1_000_000
    while high * high <= n:  # locate upper/lower bounds
        # low = high
        high *= high
    while high - low > 1:
        mid = low + ((high - low) >> 1)  # divide by 2 by bit-shifting
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low, n - low * low)


N = 100000
n = 12345678901234567890

print(timeit.timeit(stmt='isqrt({})'.format(n), setup='from math import isqrt', number=N))


stmt = """
integer_sqrt({})
""".format(n)

setup = """
def integer_sqrt(n: int) -> int:
    low = 0
    high = 10
    while high * high <= n:
        high *= high
    while high - low > 1:
        mid = low + (high - low) // 2
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low, n - low * low)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def integer_sqrt(n: int) -> int:
    low = 0
    high = 10
    while high * high <= n:
        low = high
        high *= high
    while high - low > 1:
        mid = low + (high - low) // 2
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low, n - low * low)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def integer_sqrt(n: int) -> int:
    low = 0
    high = 10
    while high * high <= n:
        high *= high
    while high - low > 1:
        mid = low + ((high - low) >> 1)
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low, n - low * low)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def integer_sqrt(n: int) -> int:
    low = 0
    high = 1_000_000
    while high * high <= n:
        high *= high
    while high - low > 1:
        mid = low + ((high - low) >> 1)
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low, n - low * low)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def integer_sqrt(n: int) -> int:
    low = 0
    high = 10
    while high * high <= n:
        low = high
        high *= high
    while high - low > 1:
        mid = low + ((high - low) >> 1)
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low, n - low * low)
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))