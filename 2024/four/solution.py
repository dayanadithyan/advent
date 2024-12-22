import numpy as np
import time


# run in function
def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_word_in_grid(grid, word):
    """
 Treats input as a matrix
 Eigenvectors of vectorizied 'XMAS' 
 Eliminate null space so to avoid traversing dead spans
 Count # of eigenvectors
 That should be same as answer 

    """
    start_time = time.time()  # timing

    # define directions: (dx, dy) as vector fields for traversal
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  
    # horizontal, vertical, main, anti-diagonal vector transformation

    # Reverse the word for backward search for isometric vector
    word_rev = word[::-1]  
    # invariance in reverse traversal

    # vectorize
    grid_array = np.array([list(row) for row in grid])
    height, width = grid_array.shape

    count = 0  # counter

    grid_processing_time = time.time() - start_time
    print(f"Grid preprocessing completed in {grid_processing_time:.4f} seconds.")

    # search
    search_start_time = time.time()

    for i in range(height):
        for j in range(width):
            for dx, dy in directions:
                #  boundary constraints for vectors (span)
                if (0 <= i + dx * (len(word) - 1) < height and
                        0 <= j + dy * (len(word) - 1) < width):
                    
                    #  indices for forward traversal
                    indices = [(i + k * dx, j + k * dy) for k in range(len(word))]
                    
                    # extract characters 
                    forward_check = ''.join(grid_array[x, y] for x, y in indices)

                    if forward_check == word:
                        count += 1  # match found in forward direction

                    # reverse check symmetry (avoids redundant checks for symmetrical cases)
                    if forward_check[::-1] == word and (dx != 0 or dy != 0):
                        count += 1  # match found in reverse direction

    search_time = time.time() - search_start_time
    print(f"Search completed in {search_time:.4f} seconds.")

    return count

# run via terminnal tho cause memory

if __name__ == "__main__":
    overall_start_time = time.time()

    file_path = "input.txt" 

    grid = read_grid_from_file(file_path)

    # search
    word = "XMAS" #string

    # run
    occurrences = find_word_in_grid(grid, word) #para:2

    print(f"Number of eigenvectors equals {occurrences} ")

    # total time
    overall_time = time.time() - overall_start_time
    print(f"Total execution time: {overall_time:.4f} seconds.")
