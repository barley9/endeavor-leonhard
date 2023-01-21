import math


def area(a: int, b: int, c: int) -> float:
    """Returns the area of the triangle with side lengths (a, b, c) using Heron's formula. See <en.wikipedia.org/wiki/Heron's_formula>"""
    s = 0.5 * (a + b + c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# TODO: this solution takes about 5 minutes to run, but it does finish and give the correct answer

maxp = 10 ** 9
total_perimeter = 0
triangles = []
for a in range(3, (maxp + 1) // 3):
    v_plus  = ((a - 1) * (a + 1) * (a + 1) * (3 * a + 1)) >> 4  # divide by 16 by bit-shifting right
    v_minus = ((a + 1) * (a - 1) * (a - 1) * (3 * a - 1)) >> 4

    sqrt_plus  = math.isqrt(v_plus)
    sqrt_minus = math.isqrt(v_minus)

    if sqrt_plus * sqrt_plus == v_plus:
        total_perimeter += 3 * a + 1
        triangles.append((a, a, a + 1))
    if sqrt_minus * sqrt_minus == v_minus:
        total_perimeter += 3 * a - 1
        triangles.append((a, a, a - 1))

print(total_perimeter)
print(triangles)