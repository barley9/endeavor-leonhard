import decimal
import math

import utils.misc


def is_square(n: int, EPSILON: float=10 ** -7) -> bool:
    """Returns True if n is a perfect square, False otherwise"""
    s = math.sqrt(n)
    return s - int(s) < EPSILON

decimal.getcontext().prec = 110  # need more than 100 digits so that 100th digit is accurate

total = 0
for i in range(1, 100 + 1):
    if is_square(i):  # only consider irrational square roots
        continue
    s = decimal.Decimal(i).sqrt()
    total += sum(utils.misc.get_digits(s)[:100])  # compute sum of first 100 digits

print("The total of the digital sums is", total)