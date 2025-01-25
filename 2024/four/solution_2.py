def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def mas(grid, r, c):
    if grid[r][c] != 'A':
        return False
    return (
        (grid[r - 1][c - 1] == 'M' and grid[r + 1][c + 1] == 'S')
        or (grid[r - 1][c - 1] == 'S' and grid[r + 1][c + 1] == 'M')
    ) and (
        (grid[r - 1][c + 1] == 'M' and grid[r + 1][c - 1] == 'S')
        or (grid[r - 1][c + 1] == 'S' and grid[r + 1][c - 1] == 'M')
    )

def main():
    grid = read_grid_from_file("input.txt")
    part2 = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[r]) - 1):
            if mas(grid, r, c):
                part2 += 1
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()