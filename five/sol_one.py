import os
from collections import defaultdict
from typing import List

# Read and process input file
with open("input.txt", "r") as file:
    inputs = file.read().split(os.linesep * 2)

pairs = [
    list(map(int, line.split("|")))
    for line in inputs[0].split(os.linesep)
]

lists = [
    list(map(int, line.split(",")))
    for line in inputs[1].split(os.linesep)
]

# Group pairs by their second value and create a dictionary
prefixes = defaultdict(list)
for pair in pairs:
    prefixes[pair[1]].append(pair[0])

# Custom comparator function
def compare(x, y):
    return -1 if y in prefixes.get(x, []) else 1

# Function to get the middle element of a list
def middle(lst: List[int]) -> int:
    return lst[len(lst) // 2]

part1 = 0
part2 = 0

# Process lists
for lst in lists:
    for i in range(len(lst)):
        if lst[i] not in prefixes:
            continue
        if any(item in prefixes[lst[i]] for item in lst[i + 1:]):
            lst.sort(key=lambda x: (x, compare(lst[0], x)))  # Sorting with custom comparator
            part2 += middle(lst)
            break
    else:
        part1 += middle(lst)

# Print results
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
