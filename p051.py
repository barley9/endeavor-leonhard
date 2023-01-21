import numpy as np

import utils.primes
import utils.misc


def replace(n: int, d: int, locations: tuple) -> int:
    """Replaces the digits of `n` with the digit `d` at the place values specified in `locations`"""
    strn = str(n)[::-1]
    strd = chr(d + ord('0'))
    return int(''.join((strd if i in locations else strn[i]) for i in range(len(strn) - 1, -1, -1)))

def are_siblings(n: int, m: int) -> bool:
    return '0' in '{0:0{length}d}'.format(abs(n - m), length=max(len(str(n)), len(str(m))))

def get_families(n: int) -> list:
    families = []

    # get array of digits of n in order of increasing place value
    digit_list = utils.misc.int2digits(n)

    # pre-generate array of digit replacements
    replacements = np.tile(np.arange(10), (len(digit_list), 1)).T

    digit_mask = np.zeros(shape=len(digit_list), dtype=bool)  # construct array to mask off digits of n
    for mask in range(1, 2 ** len(digit_list) - 1):  # for each valid bit mask over the digits of n...
        digit_mask[:] = [(mask >> k) & 1 for k in range(len(digit_list))]  # ...set elements of boolean array to mask bits...
        # replace masked digits of n, skipping 0 if most significant mask bit is set
        family = set()
        for digit_straight in (replacements[1:] if digit_mask[-1] else replacements):
            family.add(utils.misc.digits2int(np.where(digit_mask, digit_straight, digit_list)))  # convert list of digits back to int and append to families
        families.append(family)

    return families

if __name__ == '__main__':
    primes = utils.primes.prime_sieve(1_000_000)[4:]  # skip 2, 3, 5, and 7
    primes_set = set(primes)

    max_family_size = 0
    for n in primes:
        fams = get_families(n)
        for fam in fams:
            prime_members = fam & primes_set
            if len(prime_members) > max_family_size:
                max_family_size = len(prime_members)
                print(prime_members)
                if len(prime_members) > 7:
                    break
        else:
            continue
        break

    print("The smallest prime in an 8-member family is {}.".format(sorted(prime_members)[0]))