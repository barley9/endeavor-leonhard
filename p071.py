from fractions import Fraction


def mediant(a: Fraction, b: Fraction) -> Fraction:
    """Calculates the 'mediant' or 'freshman sum' of two fractions. See <en.wikipedia.org/wiki/Mediant_(mathematics)>"""
    return Fraction(a.numerator + b.numerator, a.denominator + b.denominator)

def left_nearest_neighbor(right: Fraction, maximum_denominator: int) -> Fraction:
    left = Fraction(0)

    temp = left
    while temp.denominator <= maximum_denominator:
        left = temp
        temp = mediant(left, right)

    return left
    

if __name__ == '__main__':
    threeSevenths = Fraction(3, 7)
    dmax = 1_000_000
    lnn = left_nearest_neighbor(threeSevenths, dmax)
    
    print("The fraction immediately to the left of {} is {}.".format(threeSevenths, lnn))
