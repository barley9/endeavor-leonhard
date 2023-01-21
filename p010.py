import utils.primes

N = 2_000_000
ps = utils.primes.prime_sieve(N)
print("The sum of primes below {:_} is {}.".format(N, sum(ps)))