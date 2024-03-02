with open('input4.txt', 'r') as file:
    numbers = [int(i) for i in file.read().split() if i.strip()]

sum_numbers = sum(numbers)

with open('output.txt', 'w') as file:
    file.write(str(sum_numbers))
