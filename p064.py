import itertools
import decimal
decimal.getcontext().prec = 1000

import utils.contfrac
import utils.misc

# TODO: this takes forever and isn't even correct; probably need higher precision

N = 10000
count = 0
s = set(range(2, N + 1)) - set(i * i for i in range(2, utils.misc.isqrt(N) + 1))  # remove squares
for n in s:
    sqrtn = decimal.Decimal(n).sqrt()
    coefs = utils.contfrac.coefficients(sqrtn)
    cyc = utils.misc.get_cycle(coefs[1:200])
    if len(cyc) % 2 == 1:
        count += 1
        print(n, len(cyc), str(cyc[:20])[:-1] + (']' if len(cyc) <= 20 else ', ...]'))

print("odd cycle len:", count)
