"""
     1  /           _________________  \
b = --- | 1 +/- _  / 1 + 2 n (n - 1)   |
     2  \        \/                    /

b = number of blue disks
n = total number of disks
"""

import itertools

N = 1_000  # 1_000_000_000_000

odd_squares = (i * i for i in itertools.count(N + 1, skip=2))

for _ in range(10):
    print(next(odd_squares))