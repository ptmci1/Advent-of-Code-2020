# AoC 2020 Puzzle 3


# Reading input from text file, converting to array
def read_file():
    input_raw = open("Input3.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_raw.close()
    return input_arr


def solve1(input_arr):
    acc = 0
    x_axis = 0
    switch = {
        28: -3,
        29: -2,
        30: -1
    }
    for elem in input_arr:
        # print(x_axis)
        if list(elem)[x_axis] == '#':
            acc += 1
        x_axis = switch.get(x_axis, x_axis) + 3
    return acc


print(solve1(read_file()))
