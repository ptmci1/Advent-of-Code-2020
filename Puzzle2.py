# AoC 2020 Puzzle 2


# Reading input from text file, converting to array of ints
def read_file():
    input_raw = open("Input2.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_raw.close()
    return input_arr


def solve(input_arr):
    acc = 0
    for elem in input_arr:
        low_bound = elem.split('-')[0]
        high_bound = elem.split()[0].split('-')[1]
        target = list(elem.split()[1])[0]
        password = elem.split()[2]
        if int(high_bound) >= password.count(target) >= int(low_bound):
            acc += 1
    return acc


print(solve(read_file()))
