from collections import Counter
import pprint

with open("input.txt", "r") as file:
    text = file.read()
    text = text.lower()
    character_count = Counter(text)
    pprint.pprint(character_count)
