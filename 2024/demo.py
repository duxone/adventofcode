import numpy as np
import pandas as pd
import regex as re
from advent_core import AdventOfCode

DAY = 1

def convert_numbers(text):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    pattern = r'(?:\d|zero|one|two|three|four|five|six|seven|eight|nine)'
    matches = re.findall(pattern, text.lower(), overlapped=True)
    
    result = ''
    for match in matches:
        if match.isdigit():
            result += match
        else:
            result += number_map[match]
    
    return result

def solve_part_one(input_data):
    pattern = r'\d'
    parsed_input = []
    for seq in input_data.splitlines():            
        parsed_input.append(''.join(re.findall(pattern, seq)))
    return sum(int(x[0] + x[-1]) for x in parsed_input)   

def solve_part_two(input_data):
    parsed_input = []
    for seq in input_data.splitlines():
        parsed_input.append(convert_numbers(seq))
    return sum(int(x[0] + x[-1]) for x in parsed_input)
            
    #print(f"\nSolution for part 1: {solution_part2}")
    #aoc.save_solution(1, 1, str(solution_part2))
    
    # Later, retrieve the solution
    #saved_solution = aoc.get_solution(1, 1)


    #print(f"\nSaved solution for part 1: {saved_solution}")

if __name__ == "__main__":
    display_problem = False
    aoc = AdventOfCode(year=2023)
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

    print(f"\nThe solution for {DAY}/{aoc.year} is:")
    print(solve_part_one(input_data))

    print(f"\nThe solution for {DAY}/{aoc.year} is:")
    print(solve_part_two(input_data))

