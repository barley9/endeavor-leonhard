import math
import functools

import utils.primes


def cat(m: int, n: int) -> int:
    """Returns the integer formed by concatenating the digits of `m` and `n`"""
    return int(str(m) + str(n))

@functools.lru_cache(maxsize=2 ** 20)
def is_prime(n: int) -> bool:
    """Hybrid primality test"""
    global pmax
    global primes
    global primes_set

    if n < pmax:
        return n in primes_set
    else:
        sqrtn = math.sqrt(n)
        for i in primes:
            if i > sqrtn:
                break
            elif n % i == 0:
                return False
        return True

global pmax
global primes
global primes_set

pmax = 200_000_000

print("generating set of primes...")
primes = [int(p) for p in utils.primes.prime_sieve(pmax)]
primes_set = set(primes)

print("searching for prime pair sets...")  # NOTE: this takes over 15 minutes to run
pair_sets = []
for prime in primes:
    for s in pair_sets:
        if all(is_prime(cat(prime, p)) and is_prime(cat(p, prime)) for p in s):
            s.append(prime)
            if len(s) > 3:
                print(s)
    pair_sets.append([prime])

# >>> Found set of size 5 [5381, 5507, 7877, 41621, 47237] with sum 107623.  # NOTE: this is wrong; try splitting primes instead of building them up?