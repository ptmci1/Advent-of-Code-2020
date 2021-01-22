# AoC 2020 Puzzle 2


# Reading input from text file, converting to array of ints
def read_file():
    input_raw = open("Input2.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_raw.close()
    return input_arr


def solve1(input_arr):
    acc = 0
    for elem in input_arr:
        low_bound = int(elem.split('-')[0])
        high_bound = int(elem.split()[0].split('-')[1])
        target = list(elem.split()[1])[0]
        password = elem.split()[2]
        if high_bound >= password.count(target) >= low_bound:
            acc += 1
    return acc


def solve2(input_arr):
    acc = 0
    for elem in input_arr:
        index1 = int(elem.split('-')[0]) - 1
        index2 = int(elem.split()[0].split('-')[1]) - 1
        target = list(elem.split()[1])[0]
        password = list(elem.split()[2])
        if password[index1] == target and password[index2] != target:
            acc += 1
        if password[index1] != target and password[index2] == target:
            acc += 1
    return acc


print(solve2(read_file()))
