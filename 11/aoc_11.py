import numpy as np
import re


def read_input():
    loc = 'aoc_11_input.txt'
    # loc = 'aoc_11_example.txt'
    # loc = 'aoc_11_example_2.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    """slow version"""
    total_blinks = 25

    stones = inputs[0].split(' ')
    for blink in range(total_blinks):
        # go through all stones
        new_stones = []
        for n in stones:
            # define rules
            if n == '0':
                n = '1'
                new_stones.append(n)
            elif len(n) % 2 == 0:
                sep = int(len(n)/2)
                n1 = str(int(n[:sep]))
                n2 = str(int(n[sep:]))
                new_stones.append(n1)
                new_stones.append(n2)
            else:
                n = str(int(n)*2024)
                new_stones.append(n)
        stones = new_stones
        print(f'blink {blink}')

    total = len(stones)
    return total


def task_02(inputs):
    """fast version"""
    total_blinks = 75

    stones = np.asarray(inputs[0].split(' '))
    total = stones.shape[0]
    appearance_mem = list(np.ones(shape=stones.shape))
    for blink in range(total_blinks):
        # go through all stones
        # remember appearances to not apply rules on two identical stones in one line twice
        # also remember which stones where created by such a shortcut
        stone_appearance_mem = {}
        for s, mem in zip(stones, appearance_mem):
            if s in stone_appearance_mem.keys():
                stone_appearance_mem[s] += mem
            else:
                stone_appearance_mem[s] = mem
        new_stones = []
        new_appearance_mem = []
        for n in stone_appearance_mem.keys():
            # define rules
            if n == '0':
                n1 = '1'
                new_stones.append(n1)
                new_appearance_mem.append(stone_appearance_mem[n])
            elif len(n) % 2 == 0:
                sep = int(len(n)/2)
                n1 = str(int(n[:sep]))
                n2 = str(int(n[sep:]))
                new_stones.append(n1)
                new_stones.append(n2)
                new_appearance_mem.append(stone_appearance_mem[n])
                new_appearance_mem.append(stone_appearance_mem[n])
                total += stone_appearance_mem[n]
            else:
                n1 = str(int(n)*2024)
                new_stones.append(n1)
                new_appearance_mem.append(stone_appearance_mem[n])
        stones = np.asarray(new_stones)
        appearance_mem = new_appearance_mem
        print(f'blink {blink}')

    return int(total)


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
