import numpy as np
import matplotlib.pyplot as plt


def left_half_plane(p0: tuple, p1: tuple, p2: tuple) -> bool:
    """
    Returns True if `p2` lies in the half-plane to the LEFT of the vector from
    `p0` to `p1`, False otherwise

    Explanation:
    Start by finding the equation of the line connecting the points `p0` and `p1`:
          m = (y1 - y0) / (x1 - x0)
    ==>  y0 = m x0 + b
    ==>  b = (x1 y0 - x0 y1) / (x1 - x0)

    Next, test whether `p2` is above or below the line:
    ==>  y2 > m x2 + b

    After several algebraic steps, we arrive to the expression below.
    """
    return p0[0]*p1[1] + p1[0]*p2[1] + p2[0]*p0[1] > p0[0]*p2[1] + p1[0]*p0[1] + p2[0]*p1[1]


with open("0102_triangles.txt", 'r') as infile:
    triangles = [
        np.array(tuple(
            int(x)
            for x in line.strip().split(',')
        )).reshape((3, 2))
        for line in infile.readlines()
    ]

# The origin must be in the same half-plane for every pair of vertices. We
# don't know *a priori* whether the vertices are listed in clockwise or anti-
# clockwise order. But, as long as all edge vectors keep the origin on the
# same side (left or right), then the origin must be inside the triangle,
# regardless of the winding order.
total = sum(
    left_half_plane(p0, p1, (0,0)) == left_half_plane(p1, p2, (0,0)) == left_half_plane(p2, p0, (0,0))
    for p0, p1, p2 in triangles
)

print(f"The number of triangles which contain the origin is {total}")

# i = 0

# fig, ax = plt.subplots(1, 1)
# ax.add_patch(plt.Polygon(triangles[i], color='r'))
# plt.scatter(x=[(0,)], y=[(0,)], s=100, color='k')
# plt.show()