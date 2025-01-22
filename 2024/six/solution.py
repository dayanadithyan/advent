from collections import defaultdict
from itertools import count
from cmath import rect, phase

UP = 1j
TURN_RIGHT = -1j

def part_one(input):
    map_data, start = parse(input)
    return len(walk(map_data, start)[0])

def part_two(input):
    map_data, start = parse(input)
    return sum(
        walk(map_data | {pos: '#'}, start)[1]
        for pos in walk(map_data, start)[0]
    )

def walk(map_data, pos):
    seen = set()
    direction = UP
    while pos in map_data and (pos, direction) not in seen:
        seen.add((pos, direction))
        if map_data.get(pos + direction, '.') == '#':
            direction *= TURN_RIGHT
        else:
            pos += direction
    positions = {p for p, _ in seen}
    return positions, (pos, direction) in seen

def parse(input):
    lines = input.splitlines()
    map_data = {
        -UP * y + x: char
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
    }
    start = next(pos for pos, char in map_data.items() if char == '^')
    return map_data, start

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_data = file.read().strip()

    print("Part One:", part_one(input_data))
    print("Part Two:", part_two(input_data))