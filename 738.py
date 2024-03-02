unique_words = set()

with open('input.txt', 'r') as file:
    for line in file:
        words = line.split()
        unique_words.update(words)

for word in unique_words:
    print(word)
