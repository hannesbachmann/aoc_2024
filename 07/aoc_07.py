import numpy as np
import re
import itertools


def read_input():
    loc = 'aoc_08_input.txt'
    # loc = 'aoc_08_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    input_nums = []
    options = []
    for i in inputs:
        nums = [int(d) for d in re.findall(r'[0-9]+', i)]
        input_nums.append(nums)
        options.append([c for c in itertools.product(range(2), repeat=len(nums[1:])-1)])
        pass
    total = 0
    # test all options (brute force) until one is found
    for opt, inp in zip(options, input_nums):
        sol_found = False
        test_value = inp[0]
        rest_values = inp[1:]
        for o in opt:
            if sol_found:
                break
            curr_res = rest_values[0]
            for rule, v in zip(o, rest_values[1:]):
                if sol_found:
                    break
                if rule == 0:
                    # add
                    curr_res += v
                elif rule == 1:
                    # mul
                    curr_res *= v
                # test if already larger to save time, use next combination
                if curr_res > test_value:
                    break
            if curr_res == test_value:
                sol_found = True
                break
            pass
        if sol_found:
            total += test_value
    return total


def task_02(inputs):
    total = 0
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass