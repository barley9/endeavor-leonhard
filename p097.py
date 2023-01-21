# (28433 * 2 ** 7830457 + 1) % (10 ** 10)
a = 28433
b = 7830457
dig = 10
print("The last {} digits of the prime p = {} * 2 ** {} + 1 are ...{}".format(dig, a, b, (a * 2 ** b + 1) % (10 ** dig)))