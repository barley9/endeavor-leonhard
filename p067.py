import math
import functools

import utils.figurate


def get_row_column(index: int) -> tuple:
    """returns the (row, column) of the element at index"""
    n = utils.figurate.inverse_triangle(index)

    row = math.ceil(n)
    column = index - utils.figurate.triangle(row - 1)

    return (row, column)

def get_index(row: int, column: int) -> int:
    """functional inverse of get_row_column()"""
    return utils.figurate.triangle(row - 1) + column

def get_children_indices(index: int) -> tuple:
    row, col = get_row_column(index)
    return (get_index(row + 1, col),
            get_index(row + 1, col + 1))

@functools.lru_cache
def get_maxpathsum(index: int) -> int:
    global tree_heap

    left, right = get_children_indices(index)

    if (left >= len(tree_heap)) or (right >= len(tree_heap)):
        return tree_heap[index]
    else:
        return tree_heap[index] + max(get_maxpathsum(left), get_maxpathsum(right))


if __name__ == '__main__':
    tree_string = """
    3
    7 4
    2 4 6
    8 5 9 3
    """

    with open('p067_triangle.txt', 'r') as file:  # NOTE: replace 'p067_triangle.txt' with 'p018_...' to solve problem 18
        tree_string = file.read()

    # print(tree_string)

    global tree_heap
    tree_heap = [None] + [int(i) for i in tree_string.split()]

    print("Max Path Sum:", get_maxpathsum(1))
    print(get_maxpathsum.cache_info())
