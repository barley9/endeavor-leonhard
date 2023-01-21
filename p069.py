import fractions

import numpy as np

import utils.primes


N = 1_000_000

t = utils.primes.totient_sieve(N)
n = np.arange(1, N + 1)

r = n / t  # calculate ratio n / phi(n)
m = np.amax(r)  # find maximum value
i = np.where(r == m)[0]  # find all indices where r has this maximum value

print('For n <= {:_} the maximum value of n / phi(n) is {} = {} at n = {}.'.format(
    N,
    fractions.Fraction(m).limit_denominator(100_000),
    m,
    list(i + 1)))

####################

import matplotlib.pyplot as plt

plt.plot(n, r, 'k.', markersize=0.5)
plt.plot([n[idx] for idx in i], [r[idx] for idx in i], 'r.')

plt.show()