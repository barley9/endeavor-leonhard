import itertools

# Extract all ordered pairs of digits
pairs = set()
with open('p079_keylog.txt', 'r') as file:
    for line in file:
        digits = [int(c) for c in line if c.isdigit()]
        pairs.add((digits[0], digits[1]))
        pairs.add((digits[1], digits[2]))
        pairs.add((digits[0], digits[2]))

# Compile set of all seen digits
digits = set()
for pair in pairs:
    digits.update(set(pair))

perms = list(itertools.permutations(digits))  # list all permutations of digits

# Find all permutations which are compatible with the digit ordering in the log file
for pair in pairs:
    a, b = pair
    for i in range(len(perms) - 1, -1, -1):
        j, k = None, None
        for d in range(len(perms[i])):  # get the indices of a and b within permutation
            if a == perms[i][d]:
                j = d
            elif b == perms[i][d]:
                k = d
        if (j is not None) and (k is not None) and (k < j):  # if b comes before a, permutation is incompatible
            del perms[i]

print("Assuming that each digit only appears once within the passcode, the shortest code compatible with the log file is {}.".format(''.join(str(i) for i in perms[0])))