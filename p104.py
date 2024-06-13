import itertools
import math

def fibonacci() -> int:
    a = 1
    b = 1

    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    digits = ''.join(str(n) for n in range(1, 9 + 1))
    perms = set(int(''.join(perm)) for perm in itertools.permutations(digits))
    for i, f in enumerate(fibonacci()):
        if (f % 1_000_000_000) in perms and (f // (10 ** (int(math.log10(f)) - 8))) in perms:
            print(f"k = {i + 1}, F_k = {f // (10 ** (int(math.log10(f)) - 8))}...{f % 1_000_000_000}")
            break