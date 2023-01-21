import utils.figurate


pentagons = [utils.figurate.pentagon(i) for i in range(1, 100_000)]
pentagons_set = set(pentagons)

for i in range(len(pentagons)):
    p = pentagons[i]
    for j in range(i - 1, -1, -1):
        q = pentagons[j]
        if (p + q in pentagons_set) and (p - q in pentagons_set):
            solution = [i, j]
            break
    else:
        continue
    break

i = 0
while pentagons[i] != pentagons[solution[0]] + pentagons[solution[1]]:
    i += 1
j = 0
while pentagons[j] != pentagons[solution[0]] - pentagons[solution[1]]:
    j += 1

print("P_{} + P_{} = P_{} = {},\nP_{} - P_{} = P_{} = {}".format(
    solution[0] + 1, solution[1] + 1, i + 1, pentagons[i],
    solution[0] + 1, solution[1] + 1, j + 1, pentagons[j]))