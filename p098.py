import math

with open("p098_words.txt", 'r') as file:
    words = [word[1:-1] for word in file.read().split(',')]

# print(words[:10])

ordA = ord('A')
anagram_groups = {}
for word in words:
    # Count the number of occurences of each letter in word
    counter = [0] * 26
    for c in word:
        counter[ord(c) - ordA] += 1
    counter = tuple(counter)

    # Add word to appropriate anagram group
    if counter in anagram_groups:
        anagram_groups[counter].append(word)
    else:
        anagram_groups[counter] = [word]

# Remove any groups that contain only one word
anagram_groups = {k : v for k, v in anagram_groups.items() if len(v) > 1}
print(len(anagram_groups))

squares = {i * i for i in range(10_000)}
# print(squares)
