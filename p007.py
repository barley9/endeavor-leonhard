import utils.primes


ps = utils.primes.prime_sieve(100_000_000)
k = 10_001
print("The {}st prime number is {}".format(k, ps[k - 1]))