import math

# N = 120
# B = (1 + math.sqrt(1 + 2 * N * (N - 1))) / 2

# for n in range(21, 120 + 1, 4):
#     print(n, (n * (n - 1)) % 4, (1 + math.sqrt(1 + 2 * n * (n - 1))) / 2)

n = 20
while True:
    bminus = (1 + math.sqrt(1 + 2 * n * (n - 1))) / 2
    bplus  = (1 + math.sqrt(1 + 2 * n * (n + 1))) / 2

    if math.isclose(bminus - round(bminus), 0.0):
        print(n, bminus, (bminus / n) * (bminus - 1) / (n - 1))
    if math.isclose(bplus - round(bplus), 0.0):
        print(n + 1, bplus, (bplus / (n + 1)) * (bplus - 1) / n)

    n += 4