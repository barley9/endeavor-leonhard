import math


p = 0  # power of 10 to begin search

t = 10 ** p
while True:
    arg = 2 * t * (t - 1) + 1
    root = math.isqrt(arg)
    if arg - root * root == 0:  # if 'remainder' is zero, print arrangement
        b = (1 + root) // 2
        print(b, t - b, t)
    t += 1

# print("The first valid arrangement with greater than 10 ** {} total discs has {} blue discs and {} red discs, for a total of {} discs in the box.".format(p, int(b), int(t - b), t))
