import timeit

N = 100
M = 70

setup = """
from p086 import min3
M = {}
triples = [(a, b, c) for a in range(1, M + 1)
                     for b in range(1, M + 1)
                     for c in range(1, M + 1)]
""".format(M)

print(timeit.timeit(stmt="""
for a, b, c in triples:
    m = min(a, b, c)
""", setup=setup, number=N))

print(timeit.timeit(stmt="""
for a, b, c in triples:
    m = min3(a, b, c)
""", setup=setup, number=N))