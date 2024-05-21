import math
import functools

def sequence(n: int) -> list:
    s = [n]
    # count = 0
    while n >= 8:
        icbrtn = int(math.cbrt(n))
        n -= icbrtn * icbrtn * icbrtn
        s.append(n)
        # count += 1
    s.extend([i for i in range(n - 1, -1, -1)])
    return s

def steps(n: int) -> int:
    """iterative implementation"""
    # s = [n]
    count = 0
    while n >= 8:
        icbrtn = int(math.cbrt(n))
        n -= icbrtn * icbrtn * icbrtn
        # s.append(n)
        count += 1
    # s.extend([i for i in range(n - 1, -1, -1)])
    return count + n#, s

@functools.lru_cache(maxsize=None)
def steps(n: int) -> int:
    """alternative recursive solution. faster, but cache grows quickly."""
    if n < 8:
        return n
    icbrtn = int(math.cbrt(n))
    return 1 + steps(n - icbrtn * icbrtn * icbrtn)

def total_steps(n: int) -> int:
    return sum(steps(i) for i in range(1, n))

for i in range(0, 100 + 1):
    print(f'{i: >3}', '|', f'{steps(i): >3}', sequence(i))

print('total steps:', total_steps(10 ** 2))
print(steps.cache_info())