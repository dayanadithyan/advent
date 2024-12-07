import sys
import timeit
from functools import wraps
from typing import List, Sequence, Callable, Iterator, TypeVar, Dict
from pprint import pprint

T = TypeVar('T')

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def generate_differences(sequence: Sequence[int]) -> Iterator[int]:
    return (abs(sequence[i+1] - sequence[i]) for i in range(len(sequence) - 1))

@timer
def read_sequences_from_file(filepath: str) -> List[List[int]]:
    sequences = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip():  # Skip empty lines
                sequences.append(list(map(int, line.split())))
    return sequences

@timer
def classify_sequence(sequence: Sequence[int]) -> str:
    def is_increasing(seq: Sequence[int]) -> bool:
        return all(seq[i] < seq[i+1] for i in range(len(seq) - 1))
    
    def is_decreasing(seq: Sequence[int]) -> bool:
        return all(seq[i] > seq[i+1] for i in range(len(seq) - 1))
    
    is_bounded_diff = all(1 <= diff <= 3 for diff in generate_differences(sequence))
    
    if is_bounded_diff and (is_increasing(sequence) or is_decreasing(sequence)):
        return "Based"
    return "Cringe"

@timer
def attempt_remove_and_classify(sequence: Sequence[int]) -> str:
    """
    Tries removing each integer from the sequence and checks if it becomes "Based".
    """
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i+1:]
        if classify_sequence(modified_sequence) == "Based":
            return "Based"
    return "Cringe"

@timer
def analyze_sequences(sequences: List[Sequence[int]]) -> Dict[str, Dict]:
    """
    Analyzes multiple sequences, classifying each and summarizing results.
    Also tries to move "Cringe" sequences to "Based" by removing one integer.
    """
    classification_counts = {"Based": 0, "Cringe": 0}
    classification_results = {"Based": {}, "Cringe": {}}
    
    for seq in sequences:
        classification = classify_sequence(seq)
        
        # Try to move Cringe to Based by removing one integer
        if classification == "Cringe":
            modified_classification = attempt_remove_and_classify(seq)
            classification = modified_classification
        
        classification_counts[classification] += 1
        classification_results[classification][tuple(seq)] = classification
    
    return {
        "counts": classification_counts,
        "results": classification_results
    }

@timer
def main():
    input_file = 'input.txt'
    try:
        sequences = read_sequences_from_file(input_file)
    except FileNotFoundError:
        print(f"{input_file} not found. Exiting VIM.")
        return

    if not sequences:
        print("Mongolian clusterfuck.")
        return

    analysis = analyze_sequences(sequences)
    
    print("\nSequence Analysis Results:")
    pprint(analysis["results"], width=120)
    
    print("\nClassification Counts:")
    pprint(analysis["counts"], width=120)

main()
