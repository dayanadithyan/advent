import re

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return [
            (int(nums[0]), list(map(int, nums[1:])))
            for line in f.read().splitlines()
            if (nums := re.findall(r'\d+', line))
        ]

def check1(target, acc, nums):
    if not nums:
        return target == acc
    n = nums[0]
    rest = nums[1:]
    return check1(target, acc * n, rest) or check1(target, acc + n, rest)

def check2(target, acc, nums):
    if acc > target:
        return False
    if not nums:
        return target == acc
    n = nums[0]
    rest = nums[1:]
    return (check2(target, int(f"{acc}{n}"), rest) or
            check2(target, acc * n, rest) or 
            check2(target, acc + n, rest))

def filter_valid(data, checker):
    return (target for target, nums in data if checker(target, nums[0], nums[1:]))

def part_one(data):
    return sum(filter_valid(data, check1))

def part_two(data):
    return sum(filter_valid(data, check2))

if __name__ == "__main__":
    input_file = "input.txt"
    data = parse_input(input_file)
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))
