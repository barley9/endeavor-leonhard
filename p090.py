"""
Graph of connected digits:
(each edge represents a square number that contains the connected digits)

8 --- 1 --- 0
      |   /  \
      |  /    \
3 --- 9/6 ==== 4

2 --- 5

Perhaps there's a way to systematically slice up the graph to place digits on die faces?
I think so:
    Cut each edge with an arrow.
    Put digit to left of arrow on one die, digit to right on other die.
    Repeat for all edges.
    Repeat for all 2^(# edges) configurations of arrows.

Problems:
    Possible to put more digits on die than it can hold (i.e. 6)?
    Need to account separately for "free die faces" (i.e. faces that are not determined)
    Need to account for 9/6 rotational symmetry

Because there are only 8 distinct edges (counting the double connection between
9/6 and 4 only once), there are 2**8 = 256 possible configurations of the
arrows.
"""

edges = [
    tuple(
        int(d if d != '9' else '6')  # use '6' to represent either 9 or 6
        for d in f'{n ** 2:02}'
    )
    for n in range(1, 9 + 1)
]
print(edges)

# config = 0b11111111
# dice = [set(), set()]
# for i, edge in enumerate(edges):
#     if config & (1 << i):
#         dice[0].add(edge[0])
#         dice[1].add(edge[1])
#     else:
#         dice[0].add(edge[1])
#         dice[1].add(edge[0])
# print(sorted(dice[0]), sorted(dice[1]))

solutions = set()
for config in range(2 ** (len(edges) - 1)):
    dice = [set(), set()]
    for i in range(len(edges)):
        if config & (1 << i):
            dice[0].add(edges[i][0])
            dice[1].add(edges[i][1])
        else:
            dice[0].add(edges[i][1])
            dice[1].add(edges[i][0])
    if all(len(d) <= 6 for d in dice):
        solutions.add(frozenset(frozenset(d) for d in dice))

print(len(solutions))
for s in solutions:
    print('\t', s)

def factorial(n: int) -> int:
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

# now take into account unspecified die faces
total = len(solutions)
digits = set(range(10))
for s in solutions:
    for die in s:
        free_sides = 6 - len(die)
        factorial(len(digits - die)) / factorial(len(die))
