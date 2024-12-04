from collections import Counter

with open("input2.txt", 'r') as file:
    lines = file.readlines()

# list comprehension x map
left, right = map(list, zip(*[map(int, line.strip().split()) for line in lines]))

# count the bands
right_counts = Counter(right)

# functional bros
similarity_score = sum(map(lambda n: n * right_counts[n], left))

print(similarity_score)