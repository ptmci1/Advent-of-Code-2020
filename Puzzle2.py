
# Reading input from text file, converting to array of ints
def read_file():
    input_raw = open("Input1.txt", "r")
    input_arr = input_raw.read().split('\n')
    input_arr = [int(elem) for elem in input_arr]
    input_raw.close()
    return input_arr

def solve(input_arr):
