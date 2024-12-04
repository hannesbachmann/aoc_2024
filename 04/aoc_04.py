import numpy as np
import re
from functools import reduce


def read_input():
    loc = 'aoc_04_input.txt'
    # loc = 'aoc_04_example.txt'
    file = open(loc, 'r')
    content = np.asarray([np.asarray([c for c in s.replace('\n', '')]) for s in file.readlines()])
    return content


def task_01(inputs):
    # replace irrelevant characters
    relevant_seq = 'XMAS'
    total = 0
    window_size = len(relevant_seq)
    # vertical
    for i in range(len(inputs)-(window_size-1)):
        start = i
        end = i+window_size
        current_seq = inputs[:, start:end]
        # forward
        total += sum([int(reduce(lambda a, b: a + b, row) == relevant_seq) for row in current_seq])
        # backward
        total += sum([int(reduce(lambda a, b: a + b, row[::-1]) == relevant_seq) for row in current_seq])
    # horizontal
    for i in range(len(inputs[0])-(window_size-1)):
        start = i
        end = i+window_size
        current_seq = inputs[start:end, :].T
        # forward
        total += sum([int(reduce(lambda a, b: a + b, row) == relevant_seq) for row in current_seq])
        # backward
        total += sum([int(reduce(lambda a, b: a + b, row[::-1]) == relevant_seq) for row in current_seq])
    # diagonal (top left to bottom right)
    for i in range(len(inputs) - (window_size - 1)):
        current_seq = []
        for j in range(len(inputs[0]) - (window_size - 1)):
            current_seq.append([inputs[i+k][j+k] for k in range(window_size)])
        # forward
        total += sum([int(reduce(lambda a, b: a + b, row) == relevant_seq) for row in current_seq])
        # backward
        total += sum([int(reduce(lambda a, b: a + b, row[::-1]) == relevant_seq) for row in current_seq])
    # diagonal (bottom left to top right)
    for i in range(len(inputs)-1, 4-2, -1):
        current_seq = []
        for j in range(len(inputs[0]) - (window_size - 1)):
            current_seq.append([inputs[i-k][j+k] for k in range(window_size)])
        # forward
        total += sum([int(reduce(lambda a, b: a + b, row) == relevant_seq) for row in current_seq])
        # backward
        total += sum([int(reduce(lambda a, b: a + b, row[::-1]) == relevant_seq) for row in current_seq])
    return total


def task_02(inputs):
    relevant_seq = 'MAS'
    # get 3x3 sub-matrices
    window_size = 3
    r, c = inputs.shape[0] - window_size + 1, inputs.shape[1] - window_size + 1
    # (r*c, 3, 3)
    matrices = np.asarray([np.asarray([inputs[i:i+window_size, j:j+window_size] for j in range(c)]) for i in range(r)]).reshape(r*c, window_size, window_size)
    # check diagonals (two must match)
    total = 0
    for m in matrices:
        d1 = int(reduce(lambda a, b: a + b, [m[i][i] for i in range(3)]) == relevant_seq)
        d2 = int(reduce(lambda a, b: a + b, [m[i][i] for i in range(3)][::-1]) == relevant_seq)
        d3 = int(reduce(lambda a, b: a + b, [m[i][2 - i] for i in range(3)]) == relevant_seq)
        d4 = int(reduce(lambda a, b: a + b, [m[i][2 - i] for i in range(3)][::-1]) == relevant_seq)
        if sum([d1, d2, d3, d4]) == 2:
            total += 1
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass