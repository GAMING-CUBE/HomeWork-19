with open('input5.txt', 'r') as file_a:
    lines = file_a.readlines()
    reversed_lines = reversed(lines)

    with open('output.txt', 'w') as file_b:
        for line in reversed_lines:
            file_b.write(line.strip() + '\n')
