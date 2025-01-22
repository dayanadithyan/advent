import os
from collections import defaultdict
from typing import List

def read_input(filename: str) -> tuple[List[List[int]], defaultdict]:
    with open(filename, "r") as file:
        inputs = file.readlines()

    pairs = []
    lists = []
    
    for line in inputs:
        line = line.strip()
        if not line:
            continue
            
        if "|" in line:
            a, b = line.split("|")
            pairs.append([int(a), int(b)])
        else:
            numbers = [int(x.strip()) for x in line.split(",") if x.strip()]
            if numbers:
                lists.append(numbers)

    prefixes = defaultdict(list)
    for pair in pairs:
        prefixes[pair[1]].append(pair[0])
    
    return lists, prefixes

def should_come_before(a: int, b: int, prefixes: defaultdict) -> bool:
    """Returns True if a should come before b in the ordering"""
    return b in prefixes.get(a, [])

def custom_sort(lst: List[int], prefixes: defaultdict) -> List[int]:
    """Sort the list according to the page ordering rules"""
    n = len(lst)
    result = lst.copy()
    
    # Bubble sort with custom comparison
    for i in range(n):
        for j in range(0, n-i-1):
            if should_come_before(result[j+1], result[j], prefixes):
                result[j], result[j+1] = result[j+1], result[j]
    
    return result

def middle(lst: List[int]) -> int:
    if not lst:
        return 0
    return lst[len(lst) // 2]

def solve(filename: str) -> tuple[int, int]:
    lists, prefixes = read_input(filename)
    
    part1 = 0
    part2 = 0

    for lst in lists:
        if not lst:
            continue
            
        for i in range(len(lst)):
            current = lst[i]
            if current not in prefixes:
                continue
                
            # Check if any subsequent elements are prefixes of current
            if any(should_come_before(current, x, prefixes) for x in lst[i + 1:]):
                sorted_lst = custom_sort(lst, prefixes)
                part2 += middle(sorted_lst)
                break
        else:
            part1 += middle(lst)

    return part1, part2

def main():
    try:
        part1, part2 = solve("input.txt")
        print(f"Part 1: {part1}")
        print(f"Part 2: {part2}")
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()