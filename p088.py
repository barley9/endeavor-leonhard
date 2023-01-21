import math

def product_sum_k2():
    pass

def min_product_sum(k: int) -> int:
    """Returns the minimal product-sum number of order k"""
    if k < 1:
        raise ValueError("k cannot be less than 1")
    elif k == 1:
        return 1

    s = k * [1]
    i = 0
    while True:
        if sum(s) == math.prod(s):
            return (sum(s), tuple(s))  # TODO: this solution is incorrect; it misses sets where one element is much larger than the others
        s[i] += 1
        i = (i + 1) % len(s)


if __name__ == '__main__':
    for k in range(2, 6 + 1):
        print(min_product_sum(k))