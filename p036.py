import utils.misc


N = 1_000_000

result = []
for n in range(1, N + 1):
    if utils.misc.is_palindrome(format(n, 'b')) and utils.misc.is_palindrome(str(n)):
        result.append(n)

print(result)
print("The sum of all the double-base palindromes less than {:_} is {}.".format(N, sum(result)))