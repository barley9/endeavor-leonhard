import numpy as np

import utils.primes


def is_prime_proof(n: int) -> bool:
    """Returns True if n is 'prime-proof', False otherwise. An integer is 'prime-proof' iff it is not prime and cannot be made prime by modifying any one of its digits."""
    # List the digits of n in ascending order of place-value
    dig = [ord(d) - 48 for d in str(n)[::-1]]  # ord('0') = 48; ord() is 2x faster than int()
    
    # Construct array of every possible mutation of the digits of n
    mutated = np.empty(shape=(10 * len(dig), len(dig)), dtype=np.int8)
    mutated[:] = dig
    for i in range(len(dig)):
        mutated[10 * i:10 * (i + 1), i] = np.arange(10)
    
    # For every mutation...
    for ds in mutated:
        # ...re-construct integer from the list of its digits...
        m = sum(int(d) * (10 ** k) for k, d in enumerate(ds))
        if utils.primes.is_prime(m):  # ...and check if it is prime
            return False
    return True


if __name__ == "__main__":
    primes = utils.primes.prime_sieve(100_000)
    search_primes = [int(p) for p in primes[:50]]  # TODO: this super-quadratic algorithm grinds to a halt when searching past the first ~50 primes

    squbes = []
    for i in range(len(search_primes) - 1):
        for j in range(i + 1, len(search_primes)):
            p, q = search_primes[i], search_primes[j]
            sqb1 = p * p * q * q * q  # p**2 * q**3
            sqb2 = p * p * p * q * q  # p**3 * q**2
            if '200' in str(sqb1) and is_prime_proof(sqb1):
                squbes.append(sqb1)
            if '200' in str(sqb2) and is_prime_proof(sqb2):
                squbes.append(sqb2)

    k = 200
    print("The {}th prime-proof sqube containing the contiguous sub-string '{}' is {}.".format(k, k, sorted(squbes)[k - 1]))