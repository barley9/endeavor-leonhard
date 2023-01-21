# See <www.desmos.com/calculator/36xlagpcj3> for a visualization of the three shortest-path candidates

import math
import functools

import utils.misc


def count_solutions(M: int) -> int:
    """Returns the number of cuboids with maximum dimensions (M, M, M) whose shortest path length is an integer"""
    count = 0
    for a in range(1, M + 1):
        for b in range(a, M + 1):
            for c in range(b, M + 1):  # it turns out that, with this ordering, s3 is always smallest so calling utils.misc.min3() is unnecessary
                count += utils.misc.is_square(c * c + (a + b) * (a + b))
    return count

def binary_search(low: int, high: int, func: callable, target: int) -> int:
    """Returns the smallest value x in the interval [low, high] for which func(x) >= target"""
    while (high - low) > 1:
        arg = low + (high - low) // 2  # divide search space in half
        result = func(arg)
        print('({}, {}), func({}) = {}'.format(low, high, arg, result))
        if result < target:
            low = arg
        else:
            high = arg
    return high

# TODO: This O(n^3) algorithm takes approximately 6 minutes per call of
# count_solutions(); the full binary search takes about 1 hour. Most of
# the time is actually spent in the for loops themselves.
print(binary_search(0, 2000, count_solutions, 1_000_000))
print(is_square.cache_info())