import numpy as np


def integer_spiral(n: int) -> np.ndarray:  # TODO: this fails with RecursionError for large n
    """Returns an `n` x `n` integer spiral array"""
    if n < 1:
        raise ValueError("parameter `n` must be positive")

    if n % 2 == 0:
        return _integer_spiral_even(n)
    else:
        return _integer_spiral_odd(n)

def _integer_spiral_odd(n: int) -> np.ndarray:
    if n == 1:
        return np.array([[1]])

    integers = np.arange((n - 1) * (n - 1) + 1, n * n + 1)
    result = np.empty(shape=(n, n), dtype=integers.dtype)

    result[:,0] = integers[:n]
    result[-1,1:] = integers[n:]
    result[:-1,1:] = _integer_spiral_even(n - 1)

    return result

def _integer_spiral_even(n: int) -> np.ndarray:
    integers = np.arange(n * n, (n - 1) * (n - 1), -1)
    result = np.empty(shape=(n, n), dtype=integers.dtype)

    result[:,-1] = integers[-n:]
    result[0,:-1] = integers[:-n]
    result[1:,:-1] = _integer_spiral_odd(n - 1)

    return result

def corners(n: int) -> list:
    """Returns a list of the values in the corners of the `n` x `n` integer spiral"""
    result = []
    i = (n - 2) ** 2
    for _ in range(4):
        i += n - 1
        result.append(i)
    return result


if __name__ == "__main__":
    import utils.primes

    print('instantiating primality tester...')
    is_prime = utils.primes.PrimalityTester()

    print('searching spiral diagonals for primes...')
    n = 1  # spiral square side length
    primes_count = 0
    diags_count = 1
    ratio = 1.0
    while ratio >= 0.1:
        n += 2
        diags_count += 4
        primes_count += sum(is_prime(i) for i in corners(n))
        ratio = primes_count / diags_count
    
    print(f"n = {n}, r = {primes_count} / {diags_count} = {ratio}")
    # print(integer_spiral(n))