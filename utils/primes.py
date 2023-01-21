import math
import functools

import numpy as np


@functools.lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factors(n: int) -> list:
    """Returns an unordered list of all the factors of n, including 1 and n itself"""
    if n <= 0:
        return []
    elif n == 1:
        return [1]

    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            result.append(i)
            if q != i:
                result.append(q)
    return result

def prime_factors(n: int) -> list:
    return [f for f in factors(n) if is_prime(f)]

def prime_sieve(n: int) -> np.ndarray:
    """Returns an array of all the primes less than n. See <en.wikipedia.org/wiki/Sieve_of_Eratosthenes>"""
    isprime = np.ones(shape=n // 2, dtype=bool)  # only check odd numbers
    isprime[0] = False  # 2 * 0 + 1 = 1 is not prime
    for i in range(1, int(math.sqrt(n)) // 2):  # only need to check up to sqrt(n)
        if isprime[i]:  # if 2 * i + 1 is not prime, skip it
            isprime[i::2 * i + 1] = False  # mark all multiples as composite
            isprime[i] = True  # re-mark 2 * i + 1 as prime
    return np.concatenate(([2], 2 * isprime.nonzero()[0] + 1))  # return only the values 2 * i + 1 where isprime[i] == True

class PrimalityTester():
    def __init__(self, max_prime: int=100_000_000):
        self.__pmax = max_prime
        self.__primes = dict.fromkeys(prime_sieve(self.__pmax))

    def __call__(self, n: int) -> bool:
        """Returns True if `n` is prime, False otherwise"""
        if n < self.__pmax:
            return n in self.__primes

        sqrtn = math.sqrt(n)
        if sqrtn < self.__pmax:
            for i in self.__primes:
                if i > sqrtn:
                    return True
                elif n % i == 0:
                    return False
            return True
        else:
            for i in self.__primes:  # check if any primes divide n
                if n % i == 0:
                    return False
            start = self.__pmax if (self.__pmax % 2 == 1) else (self.__pmax - 1)
            for i in range(start, int(sqrtn) + 1, 2):  # if we run out of primes, fall back to checking every odd integer
                if n % i == 0:
                    return False
            return True

@functools.lru_cache(maxsize=None)
def totient(n: int) -> int:
    """Returns Euler's totient function evauated at n. See <en.wikipedia.org/wiki/Euler's_totient_function>"""
    result = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            result += 1
    return result

def totient_sieve(n: int) -> list:
    """Returns a list of totient(i), where i ranges from 1 to n. See <en.wikipedia.org/wiki/Euler's_totient_function>"""
    result = np.arange(n + 1)
    isprime = np.ones(shape=n + 1, dtype=bool)
    isprime[:2] = False  # 0 and 1 are not prime
    for i in range(2, n + 1):
        if isprime[i]:
            isprime[i::i] = False  # mark all multiples as composite
            isprime[i] = True  # re-mark i as prime
            result[i::i] = (i - 1) * (result[i::i] // i)  # multiply by (p - 1) / p = (1 - (1 / p))
    return [int(i) for i in result[1:]]  # convert np.int32 to python int