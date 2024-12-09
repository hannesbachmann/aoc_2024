import numpy as np
import re
from functools import reduce


def read_input():
    loc = 'aoc_09_input.txt'
    # loc = 'aoc_09_example.txt'
    file = open(loc, 'r')
    content = np.asarray([np.asarray([s for s in s.replace('\n', '')]) for s in file.readlines()])
    return content


def task_01(inputs):
    inputs = inputs[0]
    nums = inputs[::2]
    spaces = inputs[1::2]
    n = 0
    new_string = [str(n) for i in range(int(nums[0]))]
    n += 1
    for i in range(spaces.shape[0]):
        for j in range(int(spaces[i])):
            new_string.append('.')
        for j in range(int(nums[i+1])):
            new_string.append(str(n))
        n += 1

    # compress result
    compressed_string = new_string
    all_num_positions = [m for m in range(len(new_string)) if new_string[m] != '.'][::-1]
    all_nums_reverse = [m for m in new_string if m != '.'][::-1]
    string_sep = [s for s in compressed_string]
    n = 0
    l = len(string_sep)
    back_n = len(string_sep)-1
    for i in range(l):
        if string_sep[i] == '.':
            s = ''.join(string_sep)
            if len(re.findall(r'[0-9]+', s)) <= 1:
                break
            string_sep[i] = all_nums_reverse[n]
            p = all_num_positions[n]
            n += 1
            string_sep[p] = '.'
            back_n -= 1
        if i % 1000 == 0:
            print(f'{i}     | {l}   | {round(i/l*100)}%')

    all_nums_final = [m for m in string_sep if m != '.']
    all_num_positions_final = [m for m in range(len(string_sep)) if string_sep[m] != '.']
    total = 0
    for num, pos in zip(all_nums_final, all_num_positions_final):
        total += int(num)*int(pos)
    print(total)
    return total


def task_02(inputs):
    total = 0
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
