
import itertools

with open("/mnt/data/input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

deltas = list(itertools.product([-1, 0, 1], repeat=2))

def xmas(grid, r, c, dr, dc):
    """Checks if the 'XMAS' pattern exists starting from grid[r][c] in direction (dr, dc)."""
    rows, cols = len(grid), len(grid[0])
    if dr == 0 and dc == 0:
        return False
    if grid[r][c] != 'X':
        return False
    for i in range(1, 4):
        nr, nc = r + i * dr, c + i * dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False
        if (i == 1 and grid[nr][nc] != 'M') or \
           (i == 2 and grid[nr][nc] != 'A') or \
           (i == 3 and grid[nr][nc] != 'S'):
            return False
    return True

def search(grid, r, c):
    """Counts the number of 'XMAS' patterns starting from grid[r][c]."""
    return sum(1 for dr, dc in deltas if xmas(grid, r, c, dr, dc))

def mas(grid, r, c):
    """Checks if the 'MAS' pattern exists centered around grid[r][c]."""
    rows, cols = len(grid), len(grid[0])
    if grid[r][c] != 'A':
        return False
    checks = [
        (grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S') or 
        (grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M'),
        (grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S') or 
        (grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M')
    ]
    return any(checks)

part1 = sum(search(grid, r, c) for r in range(len(grid)) for c in range(len(grid[0])))

part2 = sum(
    1 for r in range(1, len(grid) - 1) for c in range(1, len(grid[0]) - 1) if mas(grid, r, c)
)

(part1, part2)
