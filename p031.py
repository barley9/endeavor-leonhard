import utils.partitions


coin_values = frozenset({1, 2, 5, 10, 20, 50, 100, 200})

N = 200
print("£{} can be made {} ways with the currency {}.".format(
    N,
    len(utils.partitions.partitions_from_set(N, coin_values) | {(N,)}),
    sorted(coin_values),
))
print(utils.partitions.partitions_from_set.cache_info())