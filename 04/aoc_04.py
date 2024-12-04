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
    pass


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass