# Functions for working with Roman numerals

numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def decimal2roman(n: int) -> str:
    """Returns a string containin the minimal (i.e. shortest) form of n as represented in Roman numerals"""
    pass

def roman2decimal(r: str) -> int:
    r = r.upper()
    for i, dig in enumerate(r):
        if dig not in numerals:
            raise ValueError("invalid character '{}' detected at position {} in argument '{}'".format(dig, i, r))
    pass

if __name__ == '__main__':
    roman2decimal('iii')