import utils.number_to_words


count = 0
for i in range(1, 1000 + 1):
    count += len(utils.number_to_words.num2words(i, british=True).replace('-', '').replace(' ', ''))

print("There are {} total letters in all the numbers from 1 to 1000.".format(count))