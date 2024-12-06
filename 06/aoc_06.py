import numpy as np
import re
from functools import reduce


def read_input():
    loc = 'aoc_06_input.txt'
    # loc = 'aoc_06_example.txt'
    file = open(loc, 'r')
    content = np.asarray([np.asarray([s for s in s.replace('\n', '')]) for s in file.readlines()])
    return content


def task_01(inputs):
    # get starting position, store direction
    start_position = np.where(inputs=='^')[0][0], np.where(inputs=='^')[1][0]
    direction = '^'
    position = start_position
    # store visited informations
    visit_positions_mask = np.zeros(shape=inputs.shape)
    visit_directions_mask = np.zeros(shape=[inputs.shape[0], inputs.shape[1], 4])
    while 1:
        visit_positions_mask[position[0]][position[1]] = 1
        if direction == '^':
            # move up
            if position[0] == 0:
                break
            elif inputs[position[0]-1][position[1]] == '#':
                # turn right
                new_position = position
                new_direction = '>'
            else:
                # move fwd
                new_position = [position[0]-1, position[1]]
                new_direction = direction
            visit_directions_mask[new_position[0]][new_position[1]][0] = 1
        elif direction == 'v':
            # move down
            if position[0] == inputs.shape[0]-1:
                break
            elif inputs[position[0]+1][position[1]] == '#':
                # turn right
                new_position = position
                new_direction = '<'
            else:
                # move fwd
                new_position = [position[0]+1, position[1]]
                new_direction = direction
            visit_directions_mask[new_position[0]][new_position[1]][1] = 1
        elif direction == '>':
            # move right
            if position[1] == inputs.shape[1] - 1:
                break
            elif inputs[position[0]][position[1]+1] == '#':
                # turn right
                new_position = position
                new_direction = 'v'
            else:
                # move fwd
                new_position = [position[0], position[1]+1]
                new_direction = direction
            visit_directions_mask[new_position[0]][new_position[1]][2] = 1
        elif direction == '<':
            # move left
            if position[1] == 0:
                break
            elif inputs[position[0]][position[1]-1] == '#':
                # turn right
                new_position = position
                new_direction = '^'
            else:
                # move fwd
                new_position = [position[0], position[1]-1]
                new_direction = direction
            visit_directions_mask[new_position[0]][new_position[1]][3] = 1
        direction = new_direction
        position = new_position
        if visit_positions_mask[new_position[0]][new_position[1]] == 1 and sum(visit_directions_mask[new_position[0]][new_position[1]]) == 4:
            break

    total = visit_positions_mask.sum()
    return total


def task_02(inputs):
    # marking one field as obstacle should result in visiting a field, where the position and direction is the same as
    # already visited
    # to check:
    # place object before (in direction of guard) will result in visiting a position with the same direction as the
    # position was already visited
    # get starting position, store direction
    # Todo: additional check (what happens when placing object/turning 90degree right)
    start_position = np.where(inputs=='^')[0][0], np.where(inputs=='^')[1][0]
    direction = '^'
    position = start_position
    # store visited information
    visit_positions_mask = np.zeros(shape=inputs.shape)
    visit_directions_mask = np.zeros(shape=[inputs.shape[0], inputs.shape[1], 4])
    placed_opstacle_mask = np.zeros(shape=[inputs.shape[0], inputs.shape[1]])
    obstacle_count = 0
    while 1:
        visit_positions_mask[position[0]][position[1]] = 1
        if direction == '^':
            # mask all between two '#' with this direction
            c_p = position
            for i in range(inputs.shape[0]):
                if c_p[0]-i == -1:
                    break
                if inputs[c_p[0]-i][c_p[1]] == '#':
                    break
                visit_directions_mask[c_p[0]-i][c_p[1]][0] = 1
            for i in range(inputs.shape[0]):
                if c_p[0]+i == inputs.shape[0]:
                    break
                if inputs[c_p[0]+i][c_p[1]] == '#':
                    break
                visit_directions_mask[c_p[0]+i][c_p[1]][0] = 1
            # visit_directions_mask[position[0]][position[1]][0] = 1
            # move up
            if position[0] == 0:
                break
            elif inputs[position[0]-1][position[1]] == '#':
                # turn right
                new_position = position
                new_direction = '>'
            else:
                # move fwd
                new_position = [position[0]-1, position[1]]
                new_direction = direction
                # if visit_positions_mask[position[0]][position[1]] == 1 and \
                if visit_directions_mask[position[0]][position[1]][2] == 1:
                    placed_opstacle_mask[position[0]-1][position[1]] = 1
                    obstacle_count += 1
        elif direction == 'v':
            # mask all between two '#' with this direction
            c_p = position
            for i in range(inputs.shape[0]):
                if c_p[0]-i == -1:
                    break
                if inputs[c_p[0]-i][c_p[1]] == '#':
                    break
                visit_directions_mask[c_p[0]-i][c_p[1]][1] = 1
            for i in range(inputs.shape[0]):
                if c_p[0]+i == inputs.shape[0]:
                    break
                if inputs[c_p[0]+i][c_p[1]] == '#':
                    break
                visit_directions_mask[c_p[0]+i][c_p[1]][1] = 1
            # visit_directions_mask[position[0]][position[1]][1] = 1
            # move down
            if position[0] == inputs.shape[0]-1:
                break
            elif inputs[position[0]+1][position[1]] == '#':
                # turn right
                new_position = position
                new_direction = '<'
            else:
                # move fwd
                new_position = [position[0]+1, position[1]]
                new_direction = direction
                # if visit_positions_mask[position[0]][position[1]] == 1 and \
                if visit_directions_mask[position[0]][position[1]][3] == 1:
                    placed_opstacle_mask[position[0]+1][position[1]] = 1
                    obstacle_count += 1
        elif direction == '>':
            # mask all between two '#' with this direction
            c_p = position
            for i in range(inputs.shape[1]):
                if c_p[1]-i == -1:
                    break
                if inputs[c_p[0]][c_p[1]-i] == '#':
                    break
                visit_directions_mask[c_p[0]][c_p[1]-i][2] = 1
            for i in range(inputs.shape[1]):
                if c_p[1]+i == inputs.shape[1]:
                    break
                if inputs[c_p[0]][c_p[1]+i] == '#':
                    break
                visit_directions_mask[c_p[0]][c_p[1]+i][2] = 1
            # visit_directions_mask[position[0]][position[1]][2] = 1
            # move right
            if position[1] == inputs.shape[1] - 1:
                break
            elif inputs[position[0]][position[1]+1] == '#':
                # turn right
                new_position = position
                new_direction = 'v'
            else:
                # move fwd
                new_position = [position[0], position[1]+1]
                new_direction = direction
                # if visit_positions_mask[position[0]][position[1]] == 1 and \
                if visit_directions_mask[position[0]][position[1]][1] == 1:
                    placed_opstacle_mask[position[0]][position[1]+1] = 1
                    obstacle_count += 1
        elif direction == '<':
            # mask all between two '#' with this direction
            c_p = position
            for i in range(inputs.shape[1]):
                if c_p[1]-i == -1:
                    break
                if inputs[c_p[0]][c_p[1]-i] == '#':
                    break
                visit_directions_mask[c_p[0]][c_p[1]-i][3] = 1
            for i in range(inputs.shape[1]):
                if c_p[1]+i == inputs.shape[1]:
                    break
                if inputs[c_p[0]][c_p[1]+i] == '#':
                    break
                visit_directions_mask[c_p[0]][c_p[1]+i][3] = 1
            # visit_directions_mask[position[0]][position[1]][3] = 1
            # move left
            if position[1] == 0:
                break
            elif inputs[position[0]][position[1]-1] == '#':
                # turn right
                new_position = position
                new_direction = '^'
            else:
                # move fwd
                new_position = [position[0], position[1]-1]
                new_direction = direction
                # if visit_positions_mask[position[0]][position[1]] == 1 and \
                if visit_directions_mask[position[0]][position[1]][0] == 1:
                    placed_opstacle_mask[position[0]][position[1]-1] = 1
                    obstacle_count += 1
        direction = new_direction
        position = new_position
        if visit_positions_mask[new_position[0]][new_position[1]] == 1 and sum(visit_directions_mask[new_position[0]][new_position[1]]) == 4:
            break

    total = obstacle_count
    return total


if __name__ == '__main__':
    inputs = read_input()
    # t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass