import functools


fact = 10 * [1]  # pre-compute the factorials of the digits 0-9
for d in range(1, len(fact)):
    for i in range(d, len(fact)):
        fact[i] *= d

def get_digits(n: int) -> list:
    return [int(d) for d in str(n)]

@functools.lru_cache(maxsize=None)
def factorial_sum(n: int) -> int:
    s = 0
    for d in get_digits(n):
        s += fact[d]
    return s

def chain_length(n: int) -> int:
    seen = set()
    count = 0
    while n not in seen:
        count += 1
        seen.add(n)
        n = factorial_sum(n)
    return count


if __name__ == '__main__':
    nmax = 1_000_000 - 1

    lengths = (nmax + 1) * [0]
    for n in range(1, nmax + 1):
        lengths[n] = chain_length(n)

    maxlen = 0
    for l in lengths:
        if l > maxlen:
            maxlen = l

    count = 0
    for l in lengths:
        if l == maxlen:
            count += 1

    print('There are {} chains of length {} below n = {:_}'.format(count, maxlen, nmax + 1))
    # print(factorial_sum.cache_info())