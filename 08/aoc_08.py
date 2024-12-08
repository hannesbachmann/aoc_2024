import numpy as np
import re


def read_input():
    loc = 'aoc_08_input.txt'
    # loc = 'aoc_08_example.txt'
    # loc = 'aoc_08_example_2.txt'
    file = open(loc, 'r')
    content = np.asarray([np.asarray([s for s in s.replace('\n', '')]) for s in file.readlines()])
    return content


def task_01(inputs):
    antennas = np.delete(np.unique(inputs), np.where(np.unique(inputs) == '.'))
    all_locations = {a: [[row, col] for row, col in zip(np.where(inputs == a)[0], np.where(inputs == a)[1])] for a in antennas}

    pos_checker = lambda p1, p2: True if p1[0] == p2[0] and p1[1] == p2[1] else False

    reachable_mask = np.zeros(shape=inputs.shape)
    height, width = inputs.shape
    # check for each position, if it is reachable
    for row in range(height):
        for col in range(width):
            # check if already reachable by previous antenna
            if reachable_mask[row][col] == 1:
                continue
            exist = False
            # check reachability
            # all types of antennas
            for a in antennas:
                # all positions of that antenna
                for a_row, a_col in all_locations[a]:
                    # get requested position where a second antenna should be
                    r_req, c_req = row + (a_row - row)*2, col + (a_col - col)*2
                    # avoid same position
                    if row != r_req or col != c_req:
                        # check if one other antenna of this type is twice as far away, exists
                        exist = any([pos_checker([r_req, c_req], p2) for p2 in all_locations[a]])
                        if exist:
                            check_mask = np.zeros(shape=inputs.shape)
                            check_mask[row][col] = 1
                            check_mask[r_req][c_req] = 2
                            check_mask[a_row][a_col] = 2
                            reachable_mask[row][col] = 1
                            break
                if exist:
                    break
    total = reachable_mask.sum()
    return total


def task_02(inputs):
    antennas = np.delete(np.unique(inputs), np.where(np.unique(inputs) == '.'))
    all_locations = {a: [[row, col] for row, col in zip(np.where(inputs == a)[0], np.where(inputs == a)[1])] for a in antennas}

    pos_checker = lambda p1, p2: True if p1[0] == p2[0] and p1[1] == p2[1] else False

    reachable_mask = np.zeros(shape=inputs.shape)
    height, width = inputs.shape
    # check for each position, if it is reachable
    for row in range(height):
        for col in range(width):
            # check if already reachable by previous antenna
            if reachable_mask[row][col] == 1:
                continue
            exist = False
            # check reachability
            # all types of antennas
            for a in antennas:
                # all positions of that antenna
                for a_row, a_col in all_locations[a]:
                    # get requested position where a second antenna should be
                    if row == a_row and col == a_col:
                        continue
                    req_positions = [[int(row + ((a_row - row) / ggt((a_row - row), (a_col - col)))*i), int(col + ((a_col - col) / ggt((a_row - row), (a_col - col)))*i)] for i in range(inputs.shape[0])]
                    for pos in all_locations[a]:
                        if pos[0] == a_row and pos[1] == a_col:
                            continue
                        for req_pos in req_positions:
                            if pos_checker(pos, req_pos):
                                check_mask = np.zeros(shape=inputs.shape)
                                check_mask[row][col] = 1
                                check_mask[req_pos[0]][req_pos[1]] = 2
                                check_mask[a_row][a_col] = 2
                                reachable_mask[row][col] = 1
                                exist = True
                                break
                        if exist:
                            break
                    if exist:
                        break
                if exist:
                    break
    total = reachable_mask.sum()
    return total


def ggt(a, b):
    a = abs(a)
    b = abs(b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        if a == 0:
            return 1
        if b == 0:
            return 1
    return a


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
