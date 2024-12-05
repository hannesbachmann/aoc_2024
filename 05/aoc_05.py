import numpy as np
import re
from functools import reduce


def read_input():
    loc = 'aoc_05_input.txt'
    # loc = 'aoc_05_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    rules = []
    for line in inputs:
        if line == '':
            break
        n = [int(d) for d in re.findall(r'[0-9]+', line)]
        rules.append(n)
    orderings = []
    start_ordering = False
    for line in inputs:
        if start_ordering:
            n = [int(d) for d in re.findall(r'[0-9]+', line)]
            orderings.append(n)
        if line == '':
            start_ordering = True
    # check orderings
    mask_correct = []
    for i_o in range(len(orderings)):
        corr = True
        # check for each element of its correctly placed
        for i_d1, d1 in enumerate(orderings[i_o]):
            if corr:
                for i_d2, d2 in enumerate(orderings[i_o]):
                    if i_d1 < i_d2 and corr:
                        for r in rules:
                            if d1 == r[1] and d2 == r[0]:
                                corr = False
                                break
        mask_correct.append(corr)
    # get correct orderings from mask
    correct = []
    for m_i in range(len(mask_correct)):
        if mask_correct[m_i]:
            correct.append(orderings[m_i])
    # get middle position of the correct ones
    middles = []
    for c in correct:
        l = len(c)
        mid_pos = int(l // 2)
        middles.append(c[mid_pos])
    total = sum(middles)
    return total


def task_02(inputs):
    total = 0
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass