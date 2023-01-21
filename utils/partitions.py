import functools

import utils.figurate


@functools.lru_cache(maxsize=None)
def partitions_count(n: int) -> int:
    """Returns the number of partitions of n. See <en.wikipedia.org/wiki/Pentagonal_number_theorem>"""
    if n < 0:
        return 0
    elif n == 0:
        return 1
    
    result = 0
    
    k = 1
    p, q = 0, 0
    while p < n:
        p = utils.figurate.pentagon( k)
        q = utils.figurate.pentagon(-k)
        result += int((-1)**( k - 1)) * partitions_count(n - p)
        result += int((-1)**(-k - 1)) * partitions_count(n - q)
        k += 1

    return result

@functools.lru_cache()
def partitions(n: int) -> set:
    """Returns a set of the unique partitions of n, not including {n}. DANGER: this recursive algorithm is O(2**n) in both time and space!"""
    result = set()
    for i in range(1, n // 2 + 1):
        j = n - i
        result.add((i, j))
        result.update(tuple(sorted(seq + (j,))) for seq in partitions(i))
        result.update(tuple(sorted((i,) + seq)) for seq in partitions(j))
    return result

# def get_zero_run_lengths(n: int) -> list:
#     """Returns a list containing the lengths of runs of zeros appearing in the binary representation of n"""
#     result = []
#     count = 0
#     while n:
#         if n & 1:
#             result.append(count)
#             count = 0
#         else:
#             count += 1
#         n = n >> 1
#     return result

# # Alternative algorithm
# def partitions(n: int) -> set:
#     """Returns a set of the unique partitions of `n`"""
#     result = set()
#     for i in range(2 ** (n - 1)):
#         divs = [r + 1 for r in get_zero_run_lengths(i)]
#         result.add(tuple(sorted(divs + [n - sum(divs)])))
#     return result

@functools.lru_cache(maxsize=256)
def partitions_from_set(n: int, sizes: frozenset) -> set:
    """Returns a set of partitions of `n` where each partition element must be an element of `sizes`"""
    if n < min(sizes):
        return set()
    if n == min(sizes):
        return {(min(sizes),)}

    result = set()
    for i in sizes & set(range(1, n // 2 + 1)):  # only loop up to n / 2
        j = n - i
        if j in sizes:
            result.add((i, j)) if i < j else result.add((j, i))
            result.update(tuple(sorted(seq + (j,))) for seq in partitions_from_set(i, sizes) if all(elem in sizes for elem in seq))
        result.update(tuple(sorted((i,) + seq)) for seq in partitions_from_set(j, sizes) if all(elem in sizes for elem in seq))
    return result