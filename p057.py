from fractions import Fraction as F


class Fraction():


def add(f: tuple, g: tuple) -> tuple:
    return (f[0] * g[1] + g[0] * f[1], f[1] * g[1])

def sub(f: tuple, g: tuple) -> tuple:
    return (f[0] * g[1] - g[0] * f[1], f[1] * g[1])

def mul(f: tuple, g: tuple) -> tuple:
    return (f[0] * g[0], f[1] * g[1])

def div(f: tuple, g: tuple) -> tuple:
    return (f[0] * g[1], f[1] * g[0])