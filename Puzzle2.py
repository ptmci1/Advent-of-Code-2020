# AoC 2020 Puzzle 2


# Reading input from text file, converting to array of ints
def read_file():
    input_raw = open("Input2.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_raw.close()
    return input_arr


def solve(input_arr):
    for elem in input_arr:
        # low_bound = elem.split()
        low_bound = list(elem.split()[0])
        return low_bound


print(solve(read_file()))