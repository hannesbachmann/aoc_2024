import numpy as np
import re


def read_input():
    loc = 'aoc_15_input.txt'
    # loc = 'aoc_15_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    field = np.asarray([np.asarray([i for i in inp]) for inp in inputs if inp.startswith('#')])
    instructions = np.asarray([np.asarray([i for i in inp]) for inp in inputs[len(field)+1:]])

    position = [np.where(field=='@')[0][0], np.where(field=='@')[1][0]]
    boxes = np.where(field=='O')
    walls = np.where(field=='#')

    for instruction in instructions.flatten():
        if instruction == '^':
            f_pos = position[0]
            while True:
                f_pos = f_pos - 1
                if field[f_pos, position[1]] == '.':
                    # moving is possible
                    field[position[0], position[1]] = '.'
                    field[position[0]-1, position[1]] = '@'
                    if f_pos != position[0]-1:
                        field[f_pos, position[1]] = 'O'
                    position = [position[0]-1, position[1]]
                    break
                if field[f_pos, position[1]] == '#':
                    # nothing happens
                    break
        elif instruction == '>':
            f_pos = position[1]
            while True:
                f_pos = f_pos + 1
                if field[position[0], f_pos] == '.':
                    # moving is possible
                    field[position[0], position[1]] = '.'
                    field[position[0], position[1]+1] = '@'
                    if f_pos != position[1]+1:
                        field[position[0], f_pos] = 'O'
                    position = [position[0], position[1] + 1]
                    break
                if field[position[0], f_pos] == '#':
                    # nothing happens
                    break
        elif instruction == 'v':
            f_pos = position[0]
            while True:
                f_pos = f_pos + 1
                if field[f_pos, position[1]] == '.':
                    # moving is possible
                    field[position[0], position[1]] = '.'
                    field[position[0]+1, position[1]] = '@'
                    if f_pos != position[0]+1:
                        field[f_pos, position[1]] = 'O'
                    position = [position[0]+1, position[1]]
                    break
                if field[f_pos, position[1]] == '#':
                    # nothing happens
                    break
        elif instruction == '<':
            f_pos = position[1]
            while True:
                f_pos = f_pos - 1
                if field[position[0], f_pos] == '.':
                    # moving is possible
                    field[position[0], position[1]] = '.'
                    field[position[0], position[1]-1] = '@'
                    if f_pos != position[1]-1:
                        field[position[0], f_pos] = 'O'
                    position = [position[0], position[1] - 1]
                    break
                if field[position[0], f_pos] == '#':
                    # nothing happens
                    break
        pass

    boxes = np.where(field=='O')
    total = boxes[0].sum() * 100 + boxes[1].sum()
    return total


def task_02(inputs):
    total = 0
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
