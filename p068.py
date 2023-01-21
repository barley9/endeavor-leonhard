import itertools


N = 3
s = list(range(1, 2 * N + 1))

print('Finding solutions...')
seen = set()
solutions = []
for p in itertools.permutations(s):
    legs = frozenset([(p[i], p[N + i], p[N + i + 1]) for i in range(N - 1)] + [(p[N - 1], p[2*N - 1], p[N])])
    if legs in seen:
        continue
    seen.add(legs)

    for M in range(sum(s[:3]), sum(s[-3:]) + 1):
        if all(M == leg[0] + leg[1] + leg[2] for leg in legs):
            solutions.append((M, legs))
            print('\tM =', M, '| sides:', list(legs))

# The frozenset() destroyed the ordering of our polygon sides; this loop will recover the correct ordering
for i, (M, sides) in enumerate(solutions):
    # First convert frozenset() into list() and sort descending by first element of 3-tuples
    sides = sorted(list(sides), key=lambda t: t[0])
    
    # Form a chain where the third element of a link must be equal to the second element of the next link
    chain = [sides[0]]
    while len(chain) < len(sides):  # while we don't have all the links...
        for side in sides:  # ...search for new link to attach
            if side in chain:  # if link is already attached, skip it
                continue
            if chain[-1][2] == side[1]:  # if 3rd element of last chain link is equal to 2nd element of candidate link...
                chain.append(side)  # ... attach it to the chain
                continue

    # Replace unordered solution with ordered version
    solutions[i] = (M, chain)

# Convert list-of-lists to concatenated digit strings
digit_strings = []
for M, solution in solutions:
    digits = [digit for side in solution for digit in side]
    digit_string = ''.join(str(digit) for digit in digits)
    digit_strings.append(digit_string)

digit_strings.sort()
print("The maximum string for a {}-gon ring is '{}'".format(N, digit_strings[-1]))