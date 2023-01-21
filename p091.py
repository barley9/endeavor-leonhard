import math

import numpy as np
import matplotlib.pyplot as plt


def display_triangle_list(n: int, triangles: list):
    """Conscructs a Pyplot figure displaying the vertex pairs in `triangles` on an `n` x `n` grid"""
    grid_size = math.ceil(math.sqrt(len(triangles)))
    fig, axes = plt.subplots(nrows=grid_size, ncols=grid_size)
    ticks = np.arange(0, n + 1)
    for ax in axes.flat:
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.grid(zorder=0, linewidth=0.5)
    fig_size = fig.get_size_inches()
    fig.set_size_inches(fig_size[1], fig_size[1])  # set aspect ratio to 1

    sub = 0
    for tri in triangles:
        verts = [[0, 0], *tri]
        triangle = plt.Polygon(verts, zorder=1000, alpha=0.5, linewidth=0)
        axes[sub // grid_size, sub % grid_size].add_patch(triangle)
        sub += 1

    return fig, axes

def get_triangles_naive(n: int) -> set:
    """Loops over all possible values of x1, y1, x2, y2 and returns the set of pairs {(x1, y1), (x2, y2)} which satisfy the Pythagorean theorem"""
    result = set()
    for x1 in range(0, n + 1):
        for y1 in range(x1 == 0, n + 1):
            s1 = (x1 * x1) + (y1 * y1)
            for x2 in range(0, n + 1):
                for y2 in range(x2 == 0, n + 1):
                    if x1 == x2 and y1 == y2:
                        continue
                    s2 = (x2 * x2) + (y2 * y2)
                    s3 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
                    if (s1 + s2 == s3) or (s2 + s3 == s1) or (s3 + s1 == s2):
                        result.add(frozenset([(x1, y1), (x2, y2)]))
    return result

def get_triangles(n: int) -> list:
    """Returns a list of pairs of vertices"""
    result = []

    # Triangles with right angle at the origin
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            result.append([(x, 0), (0, y)])

    # Triangles with right angle on x-axis
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            result.append([(x, 0), (x, y)])

    # Triangles with right angle on y-axis
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            result.append([(x, y), (0, y)])

    # Other triangles
    for x1 in range(1, N + 1):
        for y1 in range(1, N + 1):
            for x2 in range(0, x1):
                y2, r = divmod(x1 * x1 - x1 * x2 + y1 * y1, y1)
                if y2 <= N and r == 0:  # make sure y2 is within the grid
                    result.append([(x1, y1), (x2, y2)])
                    result.append([(y1, x1), (y2, x2)])  # mirror image across y = x
    
    return result

def count_triangles(n: int) -> int:
    """
    Returns the number of triangles with integer coordinates contained
    within an `n` x `n` grid and having one vertex at the origin
    """
    count = 3 * n * n
    for x1 in range(1, N + 1):
        for y1 in range(1, N + 1):
            for x2 in range(0, x1):
                y2, r = divmod(x1 * x1 - x1 * x2 + y1 * y1, y1)
                if y2 <= N and r == 0:  # make sure y2 is within the grid
                    count += 2
    return count

def display_triangles(n: int):
    """
    Enumerates and renders all right triangles that
    - have integer coordinates,
    - are contained within an `n` x `n` grid,
    - and have one vertex at the origin.
    """
    if n < 2:
        raise ValueError("grid size must be at least 2")

    # Create and format pyplot figure
    fig, axes = plt.subplots(nrows=2 * n, ncols=2 * n)
    ticks = np.arange(0, n + 1)
    for ax in axes.flat:
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        if n < 6:
            ax.grid(zorder=0, linewidth=0.5)
    fig_size = fig.get_size_inches()
    fig.set_size_inches(fig_size[1], fig_size[1])  # set aspect ratio to 1

    # Triangles with right angle at the origin
    verts = [[0, 0], [0, 0], [0, 0]]
    for i, x in enumerate(range(1, n + 1)):
        verts[1] = [x, 0]
        for j, y in enumerate(range(1, n + 1)):
            verts[2] = [0, y]
            triangle = plt.Polygon(verts, zorder=1000, alpha=0.5, color='b', linewidth=0)
            axes[j, i].add_patch(triangle)

    # Triangles with right angle on x-axis
    verts = [[0, 0], [0, 0], [0, 0]]
    for i, x in enumerate(range(1, n + 1)):
        verts[1] = [x, 0]
        for j, y in enumerate(range(1, n + 1)):
            verts[2] = [x, y]
            triangle = plt.Polygon(verts, zorder=1000, alpha=0.5, color='g', linewidth=0)
            axes[j, n + i].add_patch(triangle)

    # Triangles with right angle on y-axis
    verts = [[0, 0], [0, 0], [0, 0]]
    for j, y in enumerate(range(1, n + 1)):
        verts[2] = [0, y]
        for i, x in enumerate(range(1, n + 1)):
            verts[1] = [x, y]
            triangle = plt.Polygon(verts, zorder=1000, alpha=0.5, color='r', linewidth=0)
            axes[n + j, i].add_patch(triangle)

    # Other triangles
    for x1 in range(1, n + 1):
        for y1 in range(1, n + 1):
            verts = [[0, 0], [x1, y1], [0, 0]]
            for x2 in range(0, x1):
                y2, r = divmod(x1 * x1 - x1 * x2 + y1 * y1, y1)
                if y2 > n or r != 0:  # make sure y2 is within the grid
                    continue
                verts[2] = [x2, y2]
                triangle = plt.Polygon(verts, zorder=1000, alpha=0.5, color='y', linewidth=0)
                axes[n + y1 - 1, n + x1 - 1].add_patch(triangle)
                # mirror image
                triangle = plt.Polygon([v[::-1] for v in verts], zorder=1000, alpha=0.5, color='m', linewidth=0)
                axes[n + x1 - 1, n + y1 - 1].add_patch(triangle)

    # Flip subplots grid vertically; see <stackoverflow.com/questions/22458919>
    axes_positions = np.empty(shape=axes.shape, dtype=object)
    for i in range(axes.shape[0]):
        for j in range(axes.shape[1]):
            axes_positions[i, j] = axes[i, j].get_position()
    axes_positions = np.flip(axes_positions, axis=0)
    for i in range(axes.shape[0]):
        for j in range(axes.shape[1]):
            axes[i, j].set_position(axes_positions[i, j])

    return fig, axes


if __name__ == '__main__':
    N = 50
    print("There are {} right triangles contained in a(n) {}x{} grid".format(count_triangles(N), N, N))
    # display_triangles(N)
    # plt.show()