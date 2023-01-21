import utils.partitions

N = 1_000_000

i = 0
p = 1
while p % N != 0:
    i += 1
    p = utils.partitions.partitions_count(i)

print("The smallest integer n for which p(n) is divisible by {:_} is n = {}, p(n) ~= {}".format(N, i, float(p)))
