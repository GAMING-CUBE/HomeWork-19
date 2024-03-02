import random

with open('input.txt', 'r') as file:
    lines = file.readlines()

num_words = random.randint(1, len(lines))
random_words = random.sample(lines, num_words)

for word in random_words:
    print(word.strip())
