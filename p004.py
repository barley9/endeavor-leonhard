import utils.misc


def get_largest_palindrome(digits: int) -> int:
    """
    Returns a tuple containing the largest palindrome which can be
    made from the product of two k-digit integers, as well as the two
    integers which form the product.
    """
    large = 0
    pair = [0, 0]
    for i in range(10 ** (digits - 1), 10 ** digits):
        for j in range(10 ** (digits - 1), 10 ** digits):
            ij = i * j
            if ij > large and utils.misc.is_palindrome(str(ij)):
                large = ij
                pair[:] = i, j
    return (large, *pair)

if __name__ == '__main__':
    print(get_largest_palindrome(3))