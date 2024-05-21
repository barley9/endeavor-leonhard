import numpy as np
import matplotlib.pyplot as plt


def int_dist(x: float) -> float:
    """returns the distance between `x` and the nearest integer to `x`"""
    frac_part = x - np.floor(x)
    return np.where(frac_part < 0.5, frac_part, 1.0 - frac_part)

def blancmange(x: float, N: int=64) -> float:
    return sum(int_dist((1 << n) * x) / (1 << n) for n in range(N + 1))


fig, ax = plt.subplots(1, 1)

# plot blancmange function
x = np.linspace(0, 0.5, 1_000_000).astype(np.float64)  # don't think type cast is necessary
y = blancmange(x)
ax.plot(x, y, color='m')

# draw circle
circle = plt.Circle((1/4, 1/2), 1/4, color='k', fill=False)
ax.add_patch(circle)

ax.set_aspect('equal')

plt.show()