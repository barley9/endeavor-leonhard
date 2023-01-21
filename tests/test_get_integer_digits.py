import timeit

"""
Script to test performance of different methods for converting an integer into a list of its digits
"""

N = 10000

setup = """
n = ''.join(str(i) for i in range(1, 100))
"""

stmt = """
digits = [ord(d) - 48 for d in str(n)]
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

stmt = """
digits = [ord(d) - ord('0') for d in str(n) if ord('0') <= ord(d) <= ord('9')]
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

stmt = """
digits = [ord(d) - 48 for d in str(n) if 48 <= ord(d) <= 57]
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

stmt = """
digits = [ord(d) - 48 for d in str(n) if d.isdigit()]
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))

stmt = """
ords = [ord(d) for d in str(n)]
digits = [d - 48 for d in ords if 48 <= d <= 57]
"""
print(timeit.timeit(stmt=stmt, setup=setup, number=N))