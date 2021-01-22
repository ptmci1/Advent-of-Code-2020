# AoC 2020 Puzzle 1
# Find the two numbers in text document that sum to 2020.
# Multiply those together and return the result for Part 1.
# Do the same with three numbers for Part 2.


# Reading input from text file, converting to array of ints
def read_file():
    input_raw = open("Input1.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_arr = [int(elem) for elem in input_arr]
    input_raw.close()
    return input_arr


# Using created array to resolve problem for Part 1
def solve_part_1(input_arr):
    for elem1 in input_arr:
        # elem2 iteration slice starts at elem1 index to avoid unnecessary rechecks
        for elem2 in input_arr[input_arr.index(elem1):]:
            if elem1 + elem2 == 2020:
                return elem1 * elem2


# Using created array to resolve problem for Part 2
def solve_part_2(input_arr):
    for elem1 in input_arr:
        for elem2 in input_arr[input_arr.index(elem1):]:
            for elem3 in input_arr[input_arr.index(elem2):]:
                if elem1 + elem2 + elem3 == 2020:
                    return elem1 * elem2 * elem3


print(solve_part_1(read_file()))
print(solve_part_2(read_file()))
