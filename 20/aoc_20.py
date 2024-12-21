import numpy as np
import re
import time
import itertools
from numba import jit
import threading

from a_star import a_star_search
from connected import is_connected


def read_input():
    loc = 'aoc_20_input.txt'
    # loc = 'aoc_20_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    int_conv = lambda x: 0 if x == '#' else 1
    grid = np.asarray([np.asarray([int_conv(i) for i in inp[1:-1]]) for inp in inputs[1:-1]])
    grid_str = np.asarray([np.asarray([i for i in inp[1:-1]]) for inp in inputs[1:-1]])
    blocks = np.where(grid_str=='#')
    # 1. calculate complete path
    # loop over all blocks:
    #   2. delete block if intersecting with the path twice
    #   3. get position of the two intersecting path positions
    #   4. get distance between the two path positions
    # 5. how often each shortcut distance occur

    start = (np.where(grid_str=='S')[0][0], np.where(grid_str=='S')[1][0])
    end = (np.where(grid_str=='E')[0][0], np.where(grid_str=='E')[1][0])
    path = a_star_search(grid=grid, src=start, dest=end)
    path_str = np.asarray([str(p) for p in path])

    diffs = []
    c = 0
    # pos_match = lambda p1, p2: True if p1[0] == p2[0] and p1[1] == p2[1] else False
    for bx, by in zip(blocks[0], blocks[1]):
        f = False
        neighbors = [(bx-1, by), (bx+1, by), (bx, by-1), (bx, by+1)]
        for n1 in neighbors:
            if f: break
            for n2 in neighbors:
                if f: break
                if str(n1) != str(n2):
                    # test intersection of block with two of its distinct neighbors
                    if str(n1) in path_str and str(n2) in path_str and not f:
                        a = np.where(path_str==str(n1))[0][0]
                        b = np.where(path_str==str(n2))[0][0]
                        if abs(b-a)-2 > 0:
                            c += 1
                            diffs.append(abs(b - a) - 2)
                            f = True

    s_diffs = np.sort(diffs)
    count_diffs = np.unique(s_diffs, return_counts=True)
    total = s_diffs[s_diffs >= 100].shape[0]
    return total


def task_02(inputs):
    int_conv = lambda x: 0 if x == '#' else 1
    grid = np.asarray([np.asarray([int_conv(i) for i in inp[1:-1]]) for inp in inputs[1:-1]])
    grid_str = np.asarray([np.asarray([i for i in inp[1:-1]]) for inp in inputs[1:-1]])

    start = (np.where(grid_str=='S')[0][0], np.where(grid_str=='S')[1][0])
    end = (np.where(grid_str=='E')[0][0], np.where(grid_str=='E')[1][0])
    path = a_star_search(grid=grid, src=start, dest=end)
    path_str = np.asarray([str(p) for p in path])

    diffs = []
    c = 0
    combinations = list(itertools.combinations(path, 2))
    i = 0
    for p1, p2 in combinations:
        i += 1
        c += int(fast_f(str(p1), str(p2), p1[0], p1[1], p2[0], p2[1], path_str))
        # found.append(str(p1) + '|' + str(p2))
        # found.append(str(p2) + '|' + str(p1))

    s_diffs = np.sort(diffs)
    count_diffs = np.unique(s_diffs, return_counts=True)
    total = s_diffs[s_diffs >= 100].shape[0]
    return total


@jit(nopython=True)
def fast_f(p1, p2, p1x, p1y, p2x, p2y, path_str):
    if p1 != p2:
        a = np.where(path_str == p1)[0][0]
        b = np.where(path_str == p2)[0][0]
        # a = find_first(item=p1, vec=path_str)
        # b = find_first(item=p2, vec=path_str)
        dist = abs(p1x - p2x) + abs(p1y - p2y)
        if abs(b - a) - dist >= 100 and dist < 20:  # 100
            # diffs.append(abs(b - a) - dist)
            return True
    return False


@jit(nopython=True)
def find_first(item, vec):
    """Return the index of the first occurrence of item in vec."""
    for i in range(len(vec)):
        if item == vec[i]:
            return i
    return -1


if __name__ == '__main__':
    inputs = read_input()
    # t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
