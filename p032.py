solutions = []
for a in range(1, 10000 - 1):
    stra = str(a)
    for b in range(a, 10000):
        strb = str(b)
        strab = str(a * b)
        if len(stra) + len(strb) + len(strab) != 9:
            continue
        digits = set(ord(d) - 48 for d in stra + strb + strab)
        if (len(digits) == 9) and (0 not in digits):
            solutions.append([a, b, a * b])

print(solutions)
print("The sum of all pandigital products is {}.".format(sum(set(sol[2] for sol in solutions))))