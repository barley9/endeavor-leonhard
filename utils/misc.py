import math
import functools


##### Methods related to digits of numbers #####

def get_digits(n: int) -> list:
    """Returns a list containing the digits of n"""
    return [ord(d) - 48 for d in str(n) if '0' <= d <= '9']  # 48 = ord('0'); ord() is about 2x faster than int()

def int2digits(n: int) -> list:
    """Returns a list of the digits of the `n` in increasing order of place value"""
    return [ord(d) - 48 for d in reversed(str(n))]

def digits2int(digits: list) -> int:
    """Returns the integer formed by concatenating the list of digits"""
    return sum(d * 10 ** k for k, d in enumerate(digits))


##### Methods related to sequences #####

def is_palindrome(sequence: list) -> bool:
    """
    Returns True if `sequence` is palindromic (is the same forward and reversed)
    and False otherwise. The parameter `sequence` can be any indexable datatype
    (i.e. string, list, tuple, etc.)
    """
    for i in range(len(sequence) // 2):
        if sequence[i] != sequence[len(sequence) - i - 1]:
            return False
    return True

def prod(sequence: list) -> int:
    """Returns the product of the elements in `sequence`; this is comparable in performance to math.prod()"""
    result = 1
    for i in sequence:
        # if i == 0:  # short-circuit if any element is 0
        #     return 0
        result *= i
    return result

def get_cycle(sequence: list) -> list:
    """
    Returns a list containing the longest repeating subsequence of `sequence`;
    returns [] if no subsequence exists.
    """
    for stride in range(1, len(sequence) // 2 + 1):  # sequence must contain at least 2 full cycles
        for start in range(stride):
            if any(sequence[start] != sequence[i] for i in range(start, len(sequence), stride)):
                break
        else:
            return sequence[:stride]
    return []
            
def get_delayed_cycle(sequence: list) -> list:
    """
    Returns a tuple containing an offset from the beginning of `sequence` and
    the longest repeating subsequence within `sequence`. Returns (None, []) if
    no subsequence exists.
    """
    for i in range(len(sequence) - 1):
        cyc = get_cycle(sequence[i:])
        if cyc:
            return (i, cyc)
    return (None, [])


##### Root finding methods #####

EPSILON = 10 ** -8

def sqrt(n: float) -> float:
    """
    Computes the square root of `n` using Newton's Method; this is about 40x
    slower than math.sqrt(). See <en.wikipedia.org/wiki/Newton's_method#Square_root>
    """
    if n < 0:
        raise ValueError("cannot take square root of negative number")

    x0 = 0.0
    x1 = 10.0
    while (x1 - x0 < -EPSILON) or (x1 - x0 > EPSILON):
        x0 = x1
        x1 = 0.5 * (x0 + n / x0)
    return x1

def cbrt(n: float) -> float:
    """Computes the cube root of `n` using Newton's Method"""
    x0 = 0.0
    x1 = 10.0
    while (x1 - x0 < -EPSILON) or (x1 - x0 > EPSILON):
        x0 = x1
        x1 = 0.3333333333333333 * (2 * x0 + n / (x0 * x0))
    return x1

def root(n: float, p: int) -> float:
    """Computes the `p`th-root of `n` using Newton's Method; equivalent to n ** (1 / p)"""
    if p % 2 == 0 and n < 0:
        raise ValueError("cannot take root of negative number for even p")

    x0 = 0.0
    x1 = 10.0
    while (x1 - x0 < -EPSILON) or (x1 - x0 > EPSILON):
        x0 = x1
        x1 = ((p - 1) * x0 + n / (x0 ** (p - 1))) / p
    return x1

def isqrt(n: int) -> int:
    """Returns the largest integer i such that i**2 <= n using binary search."""
    if n < 0:
        raise ValueError("cannot take square root of negative number")

    low = 0
    high = n + 1
    while high - low > 1:
        mid = low + ((high - low) >> 1)  # divide by 2 by bit-shifting
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return low


##### Other methods #####

@functools.lru_cache(maxsize=None)
def is_integer(n: float) -> bool:
    """Returns True if `n` is close to an integer, False otherwise."""
    if n < 0:
        return n - int(n) > -EPSILON
    else:
        return n - int(n) < EPSILON

@functools.lru_cache(maxsize=None)
def is_square(n: int) -> bool:
    sqrtn = math.sqrt(n)
    return sqrtn - int(sqrtn) < EPSILON

def min3(a, b, c):
    """
    Returns the minimum of the three arguments. This is slightly faster than
    calling the builtin min() with three arguments.
    """
    if a <= b:
        if a < c:
            return a
        else:
            return c
    elif a <= c:
        if a < b:
            return a
        else:
            return b
    else:
        if b < c:
            return b
        else:
            return c


if __name__ == '__main__':
    print(is_integer(-10.000000001))
    print(is_integer(10.000000001))