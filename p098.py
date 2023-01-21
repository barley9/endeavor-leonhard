with open("p098_words.txt", 'r') as file:
    words = [word[1:-1] for word in file.read().split(',')]

print(words[:10])