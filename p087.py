import math

import utils.primes

N = 50_000_000
ps = utils.primes.prime_sieve(int(math.sqrt(N)))

numbers = set()
for i in ps:
    i2 = i * i
    cond_i = (N - i2) ** (1 / 3)  # because i^2 + j^3 + k^4 < N, once j exceeds cbrt(N - i^2), i^2 + j^3 + k^4 >= N for all subsequent j and all k.
    for j in ps:
        if j > cond_i:
            break
        i2j3 = i2 + j * j * j
        cond_j = (N - i2j3) ** (1 / 4)
        for k in ps:
            if k > cond_j:
                break
            numbers.add(i2j3 + k * k * k * k)

print("There are {} prime power tripples below {:_}".format(len(numbers), N))