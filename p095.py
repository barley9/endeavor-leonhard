def divisor_sieve(n: int) -> list:
    """Returns a list containing lists of divisors for all integers less than n"""
    result = [[]] + [[1] for _ in range(1, n)]
    for i in range(2, len(result)):
        for j in range(i, len(result), i):
            result[j].append(i)
    return result

print('Creating divisors list...')
N = 1_000_000
divs = divisor_sieve(N + 1)

max_chain = []
seen = set()

print('Constructing chains...')
for i in range(1, N + 1):
    if i in seen:
        continue

    # Construct potential amicable chain beginning at i
    n = i
    chain = []
    keep = True
    while n not in chain:
        chain.append(n)
        n = sum(divs[n]) - n
        if n > N:  # discard chain if any element exceeds N
            keep = False
            break

    seen.update(chain)

    if not keep:
        continue

    # Trim off non-cycling part of chain
    k = 0
    while chain[k] != n:
        k += 1
    chain = chain[k:]

    if len(chain) > len(max_chain):
        max_chain = chain

print(max_chain)
print("The minimum element of the longest amicable chain is {}.".format(min(max_chain)))