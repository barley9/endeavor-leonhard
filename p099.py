import math


with open("p099_base_exp.txt", 'r') as file:
    lines = [line.split(',') for line in file.readlines()]

base_exp = [(int(line[0]), int(line[1])) for line in lines]
exp_log_base = [e * math.log(b) for b, e in base_exp]

row = 0
maximum = 0
for i, val in enumerate(exp_log_base):
    if val > maximum:
        maximum = val
        row = i

# print(row, base_exp[row], exp_log_base[row])
print("Row {} has the largest value".format(row + 1))