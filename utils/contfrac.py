"""
Module for working with continued fractions
"""

import decimal
import fractions


# def coefficients(r: float) -> list:
#     """
#     Generates the coefficients of the continued fraction representation of `r`.
#     Due to floating point limitations, only the first few values can be trusted.
#     """
#     EPSILON = 10 ** -7
#     a, b = divmod(decimal.Decimal(r), 1)
#     yield int(a)
#     while b > EPSILON:
#         a, b = divmod(1 / b, 1)
#         yield int(a)

def coefficients(r: float) -> list:
    """
    Returns a list of the coefficients of the continued fraction representation
    of `r`. Due to floating point limitations, only the first few elements'
    accuracy can be trusted.
    """
    EPSILON = 10 ** -7
    maxlen = decimal.getcontext().prec // 2

    a0, b0 = divmod(decimal.Decimal(r), 1)
    a = [int(a0)]
    b = [b0]
    while (b[-1] > EPSILON) and (len(b) < maxlen):
        an, bn = divmod(1 / b[-1], 1)
        a.append(int(an))
        b.append(bn)
    return a

def sqrt_coefficients(n: int) -> int:
    """
    Infinitely generates the continued fraction coefficients of sqrt(`n`). See
    <math.stackexchange.com/questions/2215918>
    """
    raise NotImplementedError

def convergent(a: list) -> fractions.Fraction:
    """Returns the `Fraction` formed from the continued fraction coefficients in `a`"""
    raise NotImplementedError


if __name__ == '__main__':
    decimal.getcontext().prec = 1000

    import itertools

    r = decimal.Decimal(50).sqrt()
    # r = 123 / 456
    print(list(itertools.islice(coefficients(r), 500)))
