import numpy as np
import re


def read_input():
    loc = 'aoc_13_input.txt'
    # loc = 'aoc_13_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines() if s.replace('\n', '') != '']
    return content


def task_01(inputs):
    games = [inputs[i:i+3] for i in range(0, len(inputs), 3)]
    games_nums = [[[int(d) for d in re.findall(r'[0-9]+', g)] for g in game] for game in games]

    # calculate number of button A or B presses
    get_a = lambda Ax, Bx, Ay, By, X, Y: (-1*Bx*Y + By*X) / (Ax*By - Bx*Ay)
    get_b = lambda Ax, Bx, Ay, By, X, Y: (Ax*Y - Ay*X) / (Ax*By - Bx*Ay)

    solvable = []
    costs = []
    for (Ax, Ay), (Bx, By), (X, Y) in games_nums:
        a = get_a(Ax, Bx, Ay, By, X, Y)
        b = get_b(Ax, Bx, Ay, By, X, Y)
        if a.is_integer() and b.is_integer() and a <= 100 and b <= 100:
            solvable.append(True)
            costs.append(a*3 + b*1)
        else:
            solvable.append(False)
        pass
    total = int(sum(costs))

    return total


def task_02(inputs):
    games = [inputs[i:i+3] for i in range(0, len(inputs), 3)]
    games_nums = [[[int(d) for d in re.findall(r'[0-9]+', g)] for g in game] for game in games]

    # calculate number of button A or B presses
    get_a = lambda Ax, Bx, Ay, By, X, Y: (-1*Bx*Y + By*X) / (Ax*By - Bx*Ay)
    get_b = lambda Ax, Bx, Ay, By, X, Y: (Ax*Y - Ay*X) / (Ax*By - Bx*Ay)

    solvable = []
    costs = []
    for (Ax, Ay), (Bx, By), (X, Y) in games_nums:
        X_new = X + 10000000000000
        Y_new = Y + 10000000000000
        a = get_a(Ax, Bx, Ay, By, X_new, Y_new)
        b = get_b(Ax, Bx, Ay, By, X_new, Y_new)
        if a.is_integer() and b.is_integer():
            solvable.append(True)
            costs.append(a*3 + b*1)
        else:
            solvable.append(False)
        pass
    total = int(sum(costs))

    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
