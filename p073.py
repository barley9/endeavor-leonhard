# from fractions import Fraction

# import prob71

# # TODO: function segfaults if maximum_denominator is greater than about 2000, even after increasing sys.setrecursionlimit()
# def count_fractions_between(
#         left: Fraction,
#         right: Fraction,
#         maximum_denominator: int) -> int:
#     med = prob71.mediant(left, right)
#     if med.denominator > maximum_denominator:
#         return 0
#     return count_fractions_between(left, med, maximum_denominator) + \
#            count_fractions_between(med, right, maximum_denominator) + 1


dmax = 12_000
flist = []
oneThird, oneHalf = 1 / 3, 1 / 2
for d in range(2, dmax + 1):
    for n in range(1, d):
        f = n / d
        if oneThird < f < oneHalf:
            flist.append(f)

print(len(set(flist)))