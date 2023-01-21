# import math

import utils.primes


dmax = 1_000_000

# count = 0
# for d in range(2, dmax + 1):  # TODO: this quadratic algorithm isn't going to cut it
#     for n in range(1, d):     #       probably need to use Euler's totient function
#         count += (math.gcd(n, d) == 1)
# print(count)

ts = utils.primes.totient_sieve(dmax)[1:]
print(sum(ts))
