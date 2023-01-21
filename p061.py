import math
import itertools

from utils.figurate import figurate as fig
from utils.figurate import inverse_figurate as ifig


# Generate all the 4-digit figurate numbers
figurates = []
for p in range(3, 8 + 1):
    figurates.append([fig(p, n) for n in range(math.ceil(ifig(p, 10**3)), math.ceil(ifig(p, 10**4)))])

# For each possible ordering of [triangles, squares, pentagons, hex's, hept's, oct's]...
chain = [0] * len(figurates)
for perm in itertools.permutations(figurates):
    for i in range(len(perm[0])):
        ms0, ls0 = divmod(perm[0][i], 100)  # get the most and least significant two digits in one operation
        for j in range(len(perm[1])):
            ms1, ls1 = divmod(perm[1][j], 100)
            if ls0 != ms1:
                continue
            for k in range(len(perm[2])):
                ms2, ls2 = divmod(perm[2][k], 100)
                if ls1 != ms2:
                    continue
                for m in range(len(perm[3])):
                    ms3, ls3 = divmod(perm[3][m], 100)
                    if ls2 != ms3:
                        continue
                    for n in range(len(perm[4])):
                        ms4, ls4 = divmod(perm[4][n], 100)
                        if ls3 != ms4:
                            continue
                        for p in range(len(perm[5])):
                            ms5, ls5 = divmod(perm[5][p], 100)
                            if ls4 == ms5 and ls5 == ms0:
                                chain = [perm[0][i], perm[1][j], perm[2][k], perm[3][m], perm[4][n], perm[5][p]]

print(chain)
print(sum(chain))