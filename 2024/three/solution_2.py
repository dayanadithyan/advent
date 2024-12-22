import re

# Read the input file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Part 1
matches1 = re.finditer(r'mul\([0-9]+,[0-9]+\)', input_text)
part1 = sum(
    int(numbers[0]) * int(numbers[1]) 
    for match in matches1 
    for numbers in [match.group()[4:-1].split(',')]
)
print(part1)

# Part 2
doos = ''.join(''.join(part.split("don't()")[0]) for part in input_text.split("do()"))
matches2 = re.finditer(r'mul\([0-9]+,[0-9]+\)', doos)
part2 = sum(
    int(numbers[0]) * int(numbers[1]) 
    for match in matches2 
    for numbers in [match.group()[4:-1].split(',')]
)
print(part2)