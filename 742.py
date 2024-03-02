with open('input6.txt', 'r') as input_file:
    date = input_file.read().strip()

while len(date) > 1:
    total = sum(int(digit) for digit in date)
    date = str(total)

with open('output.txt', 'w') as output_file:
    output_file.write(date)
