import numpy as np
import re


def read_input():
    loc = 'aoc_03_input.txt'
    # loc = 'aoc_03_example_2.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    full_content = ''
    for line in content:
        full_content += line
    return full_content


def task_01(inputs):
    matchings = re.findall(r'mul\([0-9]+,[0-9]+\)', inputs)
    num_pairs = [[int(d) for d in re.findall(r'[0-9]+', m)] for m in matchings]
    pair_mul = [d[0] * d[1] for d in num_pairs]
    total = sum(pair_mul)

    return total


def task_02(inputs):
    matchings = re.findall(r"(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", inputs)
    f = 1
    total = 0
    for m in matchings:
        if m == 'do()':
            f = 1
        elif m == "don't()":
            f = 0
        else:
            pair = [int(d) for d in re.findall(r'[0-9]+', m)]
            total += pair[0] * pair[1] * f
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs=inputs)
    t2_solution = task_02(inputs=inputs)
    pass