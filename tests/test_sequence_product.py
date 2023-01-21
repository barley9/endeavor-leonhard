"""
Script testing performance of different ways to compute the product of the elements of a list.
See also <stackoverflow.com/questions/2104782>
"""

import timeit


N = 100
size = 10000  # some methods are faster for smaller/bigger lists

stmt = """prod(it)"""

setup = """
from math import prod

it = list(range(1, {} + 1))
""".format(size)
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result

it = list(range(1, {} + 1))
""".format(size)
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
import functools

def prod(iterable):
    return functools.reduce(lambda a,b: a * b, iterable)

it = list(range(1, {} + 1))
""".format(size)
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

setup = """
import functools
import operator

def prod(iterable):
    return functools.reduce(operator.mul, iterable)

it = list(range(1, {} + 1))
""".format(size)
print(timeit.timeit(stmt=stmt, setup=setup, number=N))