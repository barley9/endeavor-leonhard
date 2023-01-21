import numpy as np


global INFINITY
INFINITY = 10 ** 7

global cache, cache_info
cache = {}
cache_info = {'hits': 0, 'misses': 0, 'size': 0}  # RYO cache because functools.lru_cache() can't ignore specific arguments

def min_path_sum(array: np.ndarray, row: int, col: int) -> int:
    """Returns the minimum path sum beginning at the element array[row][col] and ending at the bottom right"""
    global INFINITY
    global cache
    if (row, col) in cache:
        cache_info['hits'] += 1
        return cache[(row, col)]

    # Recurse if we haven't hit the edge of the matrix
    rmin = INFINITY
    cmin = INFINITY
    if row + 1 < array.shape[0]:
        rmin = min_path_sum(array, row + 1, col)
    if col + 1 < array.shape[1]:
        cmin = min_path_sum(array, row, col + 1)

    result = array[row, col] + (0 if (rmin == cmin == INFINITY) else min(rmin, cmin))
    
    # Update cache
    cache[(row, col)] = result
    cache_info['misses'] += 1
    cache_info['size'] += 1

    return result

with open('p081_matrix.txt', 'r') as file:
    rows = []
    for line in file:
        rows.append([int(i) for i in line.split(',')])

array = np.array(rows)

print("The minimal path sum is {}.".format(min_path_sum(array, 0 ,0)))
print("cache_info:", cache_info)
