import numpy as np
import re
from a_star import a_star_search


def read_input():
    loc = 'aoc_18_input.txt'
    # loc = 'aoc_18_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    mem_space = np.ones(shape=(71, 71))    # personal input grid
    # mem_space = np.ones(shape=(7, 7))      # example grid
    mem_locations = [[int(i) for i in l.split(',')][::-1] for l in inputs]
    i = 0
    src = [0, 0]
    dest = [70, 70]     # personal input destination
    # dest = [6, 6]       # example destination
    for r, c in mem_locations[:1024]:
        mem_space[r][c] = 0     # blocked cell (corrupted bit)
        pass

    src = [0, 0]
    dest = [70, 70]     # personal input destination
    # dest = [6, 6]       # example destination
    path = a_star_search(mem_space, src, dest)

    mem_copy = np.copy(mem_space)

    for r, c in path:
        mem_copy[r][c] = 2     # blocked cell (corrupted bit)
        pass

    total = len(np.where(mem_copy == 2)[0]) - 1

    return total


def task_02(inputs):
    mem_space = np.ones(shape=(71, 71))  # personal input grid
    # mem_space = np.ones(shape=(7, 7))  # example grid
    mem_locations = [[int(i) for i in l.split(',')][::-1] for l in inputs]
    i = 0
    src = [0, 0]
    dest = [70, 70]  # personal input destination
    # dest = [6, 6]  # example destination
    last_pos = None
    for r, c in mem_locations:
        mem_space[r][c] = 0  # blocked cell (corrupted bit)
        if i >= 1024:       # as known from task 1
            path = a_star_search(mem_space, src, dest)
            if path is None:
                print(f'bit {i} at position ({c}, {r})')
                last_pos = [c, r]
                break
            else:
                print(f'path until corruption {i} found')
        i += 1
        pass

    return last_pos


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
