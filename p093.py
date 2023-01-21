import operator
import itertools

import utils.misc


def minmax(array: list) -> tuple:
    """Returns a tuple containing the minimum and maximum values in `array`"""
    amin =  10 ** 7  # +infinity
    amax = -10 ** 7  # -infinity
    for i in array:
        if i < amin:
            amin = i
        if i > amax:
            amax = i
    return (amin, amax)

def longest_run(collection: set) -> int:
    """Returns the length of the longest run of consecutive integers in `collection`"""
    mn, mx = minmax(collection)
    longest = 0
    count = 0
    for i in range(mn, mx + 1):
        if i in collection:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 1
    if count > longest:
        longest = count
    return longest


if __name__ == '__main__':
    operators = [
        operator.add,
        operator.sub,
        operator.mul,
        operator.truediv]
    expression_trees = [
        lambda a, b, c, d, op0, op1, op2: op0(a, op1(b, op2(c, d))),
        lambda a, b, c, d, op0, op1, op2: op0(a, op1(op2(b, c), d)),
        lambda a, b, c, d, op0, op1, op2: op0(op1(a, b), op2(c, d)),
        lambda a, b, c, d, op0, op1, op2: op0(op1(a, op2(b, c)), d),
        lambda a, b, c, d, op0, op1, op2: op0(op1(op2(a, b), c), d)]
    digits = list(range(1, 9 + 1))

    # Helpers for 'pretty printing' the expression trees
    operator_strings = dict(zip(operators, ["+", "-", "*", "/"]))
    tree_string_templates = [
        "({a} {op0} ({b} {op1} ({c} {op2} {d})))",
        "({a} {op0} (({b} {op2} {c}) {op1} {d}))",
        "(({a} {op1} {b}) {op0} ({c} {op2} {d}))",
        "(({a} {op1} ({b} {op2} {c})) {op0} {d})",
        "((({a} {op2} {b}) {op1} {c}) {op0} {d})"]

    # Main search loop
    longest = [0, (0, 0, 0, 0)]
    for args in itertools.combinations(digits, r=4):  # (len(digits)! / r!) / (len(digits) - r)! = 126
        obtainable = set()
        for args_perm in itertools.permutations(args):  # len(args)! = 24
            for i, tree in enumerate(expression_trees):  # len(expression_trees) = 5
                for ops in itertools.product(operators, repeat=3):  # len(operators) ** repeat = 64
                    # print(tree_string_templates[i].format(
                    #     a=args_perm[0], b=args_perm[1], c=args_perm[2], d=args_perm[3],
                    #     op0=operator_strings[ops[0]],
                    #     op1=operator_strings[ops[1]],
                    #     op2=operator_strings[ops[2]]), "=", end=' ')
                    try:
                        obtainable.add(tree(*args_perm, *ops))
                        # print(tree(*args_perm, *ops))
                    except ZeroDivisionError:
                        # print("ZeroDivisionError")
                        pass
        candidate = longest_run(set(round(t) for t in obtainable if t > 0 and utils.misc.is_integer(t)))
        if candidate > longest[0]:
            longest[0] = candidate
            longest[1] = args

    print(longest)
    print("The concatenated four digits are {}{}{}{}.".format(*longest[1]))