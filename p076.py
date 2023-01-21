import utils.partitions

N = 100
print("The number n = {} can be written as a sum of at least two integers in {} different ways.".format(N, utils.partitions.partitions_count(N) - 1))
