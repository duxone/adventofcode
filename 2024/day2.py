import numpy as np
import pandas as pd
import regex as re
from advent_core import AdventOfCode

DAY = 2

def solve_part_one(input_data):
    safe, unsafe = [],[]
    for seq in input_data.splitlines():
        diffs = np.diff(np.loadtxt([seq]))
        if (
            np.all((diffs > 0) & (diffs < 4)) | 
            np.all((diffs < 0) & (diffs > -4))
            ):
            safe.append(diffs)
        else:
            unsafe.append(diffs)

    return len(safe)

def solve_part_two(input_data):
    safe = []
    for seq in input_data.splitlines():
        arr = np.loadtxt([seq])
        for i in range(-1, len(arr)):
            if i == -1:
                diffs = np.diff(arr)
            else:
                diffs = np.diff(np.delete(arr,i))
            if (
            np.all((diffs > 0) & (diffs < 4)) | 
            np.all((diffs < 0) & (diffs > -4))
            ):
                safe.append(diffs)
                break

    return len(safe)

if __name__ == "__main__":
    display_problem = True
    aoc = AdventOfCode(year=2024) 
    if not aoc.validate_session():
        print("Invalid session!")
        quit()
    
    input_data = aoc.get_input(DAY)

    if display_problem:
        problem = aoc.get_problem(DAY)
        print("Problem Description:") 
        print(problem)
        print("\nInput Data:")
        print(input_data[:100] + "...")  # Show first 100 chars

    print(f"\nThe first solution for {DAY}/{aoc.year} is:")
    solution_one = solve_part_one(input_data)
    print(solution_one)

    print(f"\nThe second solution for {DAY}/{aoc.year} is:")
    solution_two = solve_part_two(input_data)
    print(solution_two)

