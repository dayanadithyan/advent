import numpy as np
import time
from pathlib import Path
from typing import List, Tuple

class GridPatternFinder:
    def __init__(self, pattern_size: Tuple[int, int] = (3, 3)):

        self.pattern_size = pattern_size
        self._validate_pattern_size()

    def _validate_pattern_size(self) -> None:
        if not all(dim >= 3 and dim % 2 == 1 for dim in self.pattern_size):
            raise ValueError("Pattern dimensions must be odd numbers >= 3")

    @staticmethod
    def read_grid_from_file(file_path: str) -> np.ndarray:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Input file not found: {file_path}")

        with open(file_path, 'r') as file:
            grid = [list(line.strip()) for line in file if line.strip()]

        if not grid:
            raise ValueError("Empty grid in input file")
        
        if not all(len(row) == len(grid[0]) for row in grid):
            raise ValueError("Inconsistent row lengths in grid")

        return np.array(grid)

    def _check_pattern(self, window: np.ndarray) -> bool:
        center = window[1, 1]
        if center != 'A':
            return False

        corners = [window[0, 0], window[0, 2], window[2, 0], window[2, 2]]
        
        # check for M M / S S pattern
        return (
            (corners[0:2] == ['M', 'M'] and corners[2:] == ['S', 'S']) or
            (corners[0:2] == ['S', 'S'] and corners[2:] == ['M', 'M'])
        )

    def find_patterns(self, grid: np.ndarray) -> int:
        height, width = grid.shape
        pattern_height, pattern_width = self.pattern_size
        
        if height < pattern_height or width < pattern_width:
            raise ValueError(f"Grid too small. Minimum size: {self.pattern_size}")

        count = 0
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                window = grid[i-1:i+2, j-1:j+2]
                if self._check_pattern(window):
                    count += 1
        
        return count

def main() -> None:
    try:
        start_time = time.perf_counter()
        
        finder = GridPatternFinder()
        
        file_path = "input.txt"
        grid = finder.read_grid_from_file(file_path)
        load_time = time.perf_counter()
        
        occurrences = finder.find_patterns(grid)
        search_time = time.perf_counter()
        
        print(f"\nResults:")
        print(f"Found {occurrences} eigenvectors patterns")
        print(f"\nTiming:")
        print(f"Grid loading time: {load_time - start_time:.4f} seconds")
        print(f"Search time: {search_time - load_time:.4f} seconds")
        print(f"Total execution time: {search_time - start_time:.4f} seconds")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()