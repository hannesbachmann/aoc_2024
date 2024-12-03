import numpy as np


def read_input():
    loc = 'aoc_02_input.txt'
    # loc = 'aoc_02_example.txt'
    file = open(loc, 'r')
    content = [[int(n) for n in s.replace('\n', '').split(sep=' ')] for s in file.readlines()]
    return content


def task_01(inputs):
    diff = [[inputs[r][c] - inputs[r][c+1] for c in range(len(inputs[r]) - 1)] for r in range(len(inputs))]
    # allowed cases:
    # all negative (-1 to -3)
    # all positive (1 to 3)
    validate = lambda l: True if all([0 > l[i] > -4 for i in range(len(l))]) or \
                                 all([0 < l[i] < 4 for i in range(len(l))]) else False
    val = np.asarray([validate(diff[r]) for r in range(len(diff))])

    return val[val].shape[0]


def task_02(inputs):
    diff = [[inputs[r][c] - inputs[r][c+1] for c in range(len(inputs[r]) - 1)] for r in range(len(inputs))]
    # allowed cases:
    # all negative (-1 to -3)
    # all positive (1 to 3)
    validate_02 = lambda l: True if all([0 > l[i] > -4 for i in range(len(l))]) or \
                                    all([0 < l[i] < 4 for i in range(len(l))]) else False
    val = np.asarray([validate_02(diff[r]) for r in range(len(diff))])
    incorrect = [inputs[i] for i in np.where(val == False)[0]]
    additional_correct = 0
    for i, row in enumerate(incorrect):
        for c_i in range(len(row)):
            r_copy = [e for e in row]
            # remove element from copy, check afterwards
            del r_copy[c_i]
            # recalculate differences
            new_diff = [r_copy[c] - r_copy[c + 1] for c in range(len(r_copy) - 1)]
            # check
            if validate_02(new_diff):
                # print(row, '\n', new_diff)
                print(f'level: {c_i+1}, element: {row[c_i]}')
                additional_correct += 1
                break

    return val[val].shape[0] + additional_correct


if __name__ == '__main__':
    inputs = read_input()
    num_correct_01 = task_01(inputs=inputs)
    num_correct_02 = task_02(inputs=inputs)
    pass
