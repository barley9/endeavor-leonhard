import decimal

import utils.misc

decimal.getcontext().prec = 20000


N = 1000
longest = []
dmax = 0
for d in range(2, N):
    digits_list = utils.misc.get_digits(decimal.Decimal(1) / decimal.Decimal(d))
    # start, subsequence = get_delayed_cycle(digits_list)
    subsequence = utils.misc.get_cycle(digits_list[1:-2])  # last few digits might be inaccurate, so trim them off
    if len(subsequence) > len(longest):
        longest = subsequence
        dmax = d
        print(d, 1 / d, len(subsequence))

print("The value of d < {} for which 1/d contains the longest recurring cycle is d = {} with a cycle of length {}.".format(N, dmax, len(longest)))
