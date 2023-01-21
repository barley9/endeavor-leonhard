import utils.figurate


with open("p042_words.txt", 'r') as file:
    words = [word[1:-1] for word in file.read().split(',')]

# Compute sum of letter values for each word
sums = [sum(ord(letter) - ord('A') + 1 for letter in word) for word in words]

triangles = set(utils.figurate.triangle(i) for i in range(1, 100_000))  # this upper-bound is probably overkill, but whatever
count = 0
for word in sums:
    if (word in triangles):
        count += 1

print("There are {} triangle words in the list.".format(count))