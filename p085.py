def count(width: int, height: int) -> int:
    """Returns the number of rectangles contained within a grid of dimensions (width, height)"""
    total = 0
    for m in range(1, width + 1):
        for n in range(1, height + 1):
            total += (width - m + 1) * (height - n + 1)
    return total

dmax = 100
target = 2_000_000
closest = 0
dims = (0, 0)
for w in range(1, dmax):
    for h in range(w, dmax + 1):
        c = count(w, h)
        if (target - c) * (target - c) < (target - closest) * (target - closest):
            closest = c
            dims = (w, h)

print("dimensions: {}, area = {}, rectangle count: {}".format(dims, dims[0] * dims[1], closest))