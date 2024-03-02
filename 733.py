with open('input3.txt', 'r') as file:
    text = file.read()

reversed_text = text[::-1]

with open('output.txt', 'w') as file:
    file.write(reversed_text)
