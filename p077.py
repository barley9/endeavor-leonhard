import utils.partitions
import utils.primes

N = 5000

primes = frozenset(utils.primes.prime_sieve(1000))

i = 1
while True:
    prime_parts = utils.partitions.partitions_from_set(i, primes)
    if len(prime_parts) > N:
        break
    i += 1

print("The first integer which can be written as the sum of primes in over {} ways is {}".format(N, i))
print(utils.partitions.partitions_from_set.cache_info())