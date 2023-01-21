import numpy as np

import utils.primes


def are_permutations(m: int, n: int) -> bool:
    """Returns True if the digits of n and m are permutations of each other, False othewise"""
    strm, strn = str(m), str(n)
    if len(strm) != len(strn):  # inexpensive check for equal numbers of digits
        return False

    digits = 10 * [0]  # store the number of occurances of each digit 0-9
    for d in strm:
        digits[ord(d) - 48] += 1  # 48 = ord('0'); using ord() is faster than int()
    for d in strn:
        digits[ord(d) - 48] -= 1

    for d in digits:
        if d:
            return False  # if the digit counts of m and n don't match up (d != 0), they can't be permutations
    return True


if __name__ == "__main__":
    N = 10_000_000  # 10**7

    print('generating n array...')
    ns = np.arange(2, N)  # 1 < n < N
    print('computing totients...')
    ts = utils.primes.totient_sieve(N - 1)[1:]  # phi(n)
    print('computing ratios...')
    rs = ns / ts  # n / phi(n)
    print('extracting permutations...')
    ps = list(map(are_permutations, ns, ts))  # indices for which phi(n) is a permutation of n

    print('locating minimum...')
    idx = np.argmin(rs[ps])
    print("For 1 < n < {:_}, the value of n for which phi(n) is a permutation of n and n / phi(n) is at a minimum is n = {}, where phi(n) = {} and n / phi(n) = {}.".format(N, ns[ps][idx], np.array(ts)[ps][idx], rs[ps][idx]))