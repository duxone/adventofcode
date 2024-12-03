import numpy as np
import pandas as pd
import regex as re
from advent_core import AdventOfCode

DAY = 1

def solve_part_one(input_data):
    arr = np.genfromtxt([input_data])
    # numpy arr[::2] is even
    # numpy arr[1::2] is odd   
    diffs = np.abs(np.sort(arr[::2]) - np.sort(arr[1::2]))
    return sum(diffs)

def solve_part_two(input_data):
    arr = np.genfromtxt([input_data])
    uniques, unique_counts = np.unique(arr[::2], return_counts=True)
    similarity_dict = dict(zip(uniques, unique_counts))
    similarity_score = []
    for x in arr[1::2]:
        if x in similarity_dict:
            similarity_score.append(x * similarity_dict[x])
        else:
            continue

    return sum(similarity_score)

    # Later, retrieve the solution
    #saved_solution = aoc.get_solution(1, 1)
    #print(f"\nSaved solution for part 1: {saved_solution}")

if __name__ == "__main__":
    display_problem = True
    aoc = AdventOfCode(year=2024) 
    if not aoc.validate_session():
        print("Invalid session!")
        quit()
    
    input_data = aoc.get_input(DAY) # async

    if display_problem:
        problem = aoc.get_problem(DAY) # async 
        print("Problem Description:") 
        print(problem)
        print("\nInput Data:")
        print(input_data[:100] + "...")  # Show first 100 chars

    print(f"\nThe first solution for {DAY}/{aoc.year} is:")
    print(solve_part_one(input_data))

    print(f"\nThe second solution for {DAY}/{aoc.year} is:")
    print(solve_part_two(input_data))

