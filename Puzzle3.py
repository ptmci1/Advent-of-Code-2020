# AoC 2020 Puzzle 3


# Reading input from text file, converting to array
def read_file():
    input_raw = open("Input3.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_raw.close()
    return input_arr


# TODO refactor switch statement, to account for x increments other than 3
def solve1(input_arr, x_increment, y_increment):
    acc = 0
    x_axis = 0
    switch = {
        28: -3,
        29: -2,
        30: -1
    }
    for elem in input_arr:
        if y_increment % y_increment == 0:
            if list(elem)[x_axis] == '#':
                acc += 1
        x_axis = switch.get(x_axis, x_axis) + x_increment
    return acc


def solve2(input_arr):
    acc = solve1(input_arr, 1, 1)
    acc *= solve1(input_arr, 3, 1)
    acc *= solve1(input_arr, 5, 1)
    acc *= solve1(input_arr, 7, 1)
    acc *= solve1(input_arr, 1, 2)
    return acc


print(solve2(read_file()))
