import functools

import utils.misc


def square_digit_sum(n: int) -> int:
    return sum(d * d for d in utils.misc.int2digits(n))

def arrives_at_89(n: int) -> bool:  # alternative implementation
    while True:
        n = square_digit_sum(n)
        if n == 1:
            return False
        if n == 89:
            return True

@functools.lru_cache(maxsize=2 ** 20)
def arrives_at_89(n: int) -> bool:
    if n == 89:
        return True
    elif n == 1:
        return False
    else:
        return arrives_at_89(square_digit_sum(n))


if __name__ == '__main__':
    N = 10_000_000
    count = 0
    for i in range(1, N):
        count += arrives_at_89(i)
    
    print(f"There are {count} numbers below {N} which arrive at 89.")
    print(arrives_at_89.cache_info())
