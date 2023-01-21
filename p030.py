def digit_power_sum(n: int, p: int):
    """Returns the sum of the digits of `n` to the `p`th power"""
    return sum((ord(d) - 48) ** p for d in str(n))  # ord('0') = 48


if __name__ == "__main__":
    p = 5

    result = []
    for n in range(10, 10_000_000):  # TODO: find a way to determine this upper-bound without trial-and-error
        if n == digit_power_sum(n, p):
            result.append(n)

    print("There are {} numbers which are equal to the sum of the {}th power of their digits. Their sum is {}.".format(len(result), p, sum(result)))