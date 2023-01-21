_digit_words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
_teens_words = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}
_mult10_words = {
    0: '',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',  # not spelled 'fourty'!!!!
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}
_bignum_words = {
    0: '',
    1: 'thousand',
    2: 'million',
    3: 'billion',
    4: 'trillion',
    5: 'quadrillion',
    6: 'sextillion',
    7: 'septillion',
    8: 'octillion',
    9: 'nonillion',
    10: 'decillion',
}

def _chunk2words(n: list, british: bool) -> str:
    """For internal module use only. Given a list `n` of three digits in ascending place-value order, returns the name of the number formed by the digits"""
    result = ''
    if n[1] == 0:
        result += _digit_words[n[0]]
    elif n[1] == 1:
        result += _teens_words[n[0]]
    else:
        result += _mult10_words[n[1]] + ('-' if n[0] else '') + _digit_words[n[0]]

    return _digit_words[n[2]] + (' hundred' + (' and' if british and result else '') if n[2] else '') + (' ' if result and n[2] else '') + result


def num2words(n: int, british: bool=False) -> str:
    """Returns the name of the integer `n` in words. If `british` is True, will add 'and' after hundreds."""
    if type(n) != type(1):
        raise TypeError("argument must be an integer")
    if n == 0:
        return 'zero'
    if n < 0:
        return 'negative ' + num2words(-n)
    if n >= 10 ** (3 * (max(_bignum_words.keys()) + 1)):
        raise NotImplementedError("argument cannot exceed 10**{} - 1".format(3 * (max(_bignum_words.keys()) + 1)))

    digits = [int(d) for d in str(n)[::-1]]  # list digits of n in ascending order of place-value
    digits = digits + (-len(digits) % 3) * [0]  # pad digit list to make length a multiple of 3

    result = _chunk2words(digits[:3], british=british)
    for i in range(1, len(digits) // 3):
        chunk = _chunk2words(digits[3 * i:3 * (i + 1)], british=british)
        result = chunk + (' ' + _bignum_words[i] if chunk else '') + (' ' if chunk and result else '') + result

    return result

if __name__ == '__main__':
    print("\nAmerican English:")
    ns = [0, 1, 342, 115, -18, 10 ** 32, int('9' * 33)]
    for n in ns:
        print(n, '=>', "'" + num2words(n) + "'")

    print("\nBritish English:")
    ns = [0, 1, 342, 115, -18, 10 ** 32, int('9' * 33)]
    for n in ns:
        print(n, '=>', "'" + num2words(n, british=True) + "'")
