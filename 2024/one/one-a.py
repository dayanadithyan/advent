import numpy as np

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    left_list, right_list = zip(*[list(map(int, line.split())) for line in lines])
    return list(left_list), list(right_list)

def calculate_list_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    distances = map(lambda x, y: abs(x - y), left_sorted, right_sorted)
    return sum(distances)

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

input_str = read_input_file('/Volumes/LNX/NEW/advent/advent/2024/one/input.txt')
left_list, right_list = parse_input(input_str)
print("Total distance:", calculate_list_distance(left_list, right_list))