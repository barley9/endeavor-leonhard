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
"""