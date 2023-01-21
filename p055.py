import utils.misc


def is_lychrel(n: int) -> bool:
    for _ in range(50):
        n += int(str(n)[::-1])
        if utils.misc.is_palindrome(str(n)):
            return False
    return True

if __name__ == '__main__':
    N = 10_000

    lychrels = []
    for i in range(1, N):
        if is_lychrel(i):
            lychrels.append(i)

    print(lychrels[:10])
    print("There are {} Lychrel numbers below {}".format(len(lychrels), N))