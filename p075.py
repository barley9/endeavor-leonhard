import functools


def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    a2, b2, c2 = a * a, b * b, c * c
    return (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)

# @functools.lru_cache()
# def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
#     return a * a + b * b == c * c

L = 12
for c in range(1, L - 1):
    for b in range(1, L - c):
        a = L - b - c
        # if is_pythagorean_triple(*sorted([a, b, c])):
        if is_pythagorean_triple(a, b, c):
            print(a, b, c)

# print(is_pythagorean_triple.cache_info())
