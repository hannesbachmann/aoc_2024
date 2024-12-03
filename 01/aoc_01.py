import numpy as np
import re


def read_input():
    loc = 'aoc_01_input.txt'
    # loc = 'aoc_01_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    num_per_line = np.asarray([np.asarray([int(d) for d in re.findall(r'[0-9]+', l)]) for l in inputs])
    left, right = num_per_line[:, 0], num_per_line[:, 1]
    l_sort, r_sort = np.sort(left), np.sort(right)
    total_dist = sum([abs(l - r) for l, r in zip(l_sort, r_sort)])

    return total_dist


def task_02(inputs):
    num_per_line = np.asarray([np.asarray([int(d) for d in re.findall(r'[0-9]+', l)]) for l in inputs])
    left, right = num_per_line[:, 0], num_per_line[:, 1]
    total = sum([d * right[right == d].shape[0] for d in left])
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
