import numpy as np
import re


def read_input():
    loc = 'aoc_17_input.txt'
    # loc = 'aoc_17_example.txt'
    file = open(loc, 'r')
    content = [s.replace('\n', '') for s in file.readlines()]
    return content


def task_01(inputs):
    registers = {'A': int(inputs[0].replace('Register A: ', '')),
                 'B': int(inputs[1].replace('Register B: ', '')),
                 'C': int(inputs[2].replace('Register C: ', ''))}
    program = [int(d) for d in inputs[4].replace('Program: ', '').split(sep=',')]
    instruction_op = [program[i:i+2] for i in range(0, len(program), 2)]

    def get_operand(op):
        if op == 0:
            res = 0
        elif op == 1:
            res = 1
        elif op == 2:
            res = 2
        elif op == 3:
            res = 3
        elif op == 4:
            res = registers['A']
        elif op == 5:
            res = registers['B']
        elif op == 6:
            res = registers['C']
        elif op == 7:
            res = None
        return res

    # define instructions
    def exe_instruction(instr, ops, register, pointer):
        op = get_operand(ops)
        if instr == 0:
            # adv
            res = int(register['A'] / (2**op))
            register['A'] = res
            return [], register, pointer+1
        elif instr == 1:
            # bxl
            res = register['B'] ^ ops
            register['B'] = res
            return [], register, pointer+1
        elif instr == 2:
            # bst
            res = op % 8
            register['B'] = res
            return [], register, pointer+1
        elif instr == 3:
            # jnz
            if register['A'] == 0:
                return [], register, pointer+1
            else:
                pointer = op // 2
                return [], register, pointer
        elif instr == 4:
            # bxc
            res = register['B'] ^ register['C']
            register['B'] = res
            return [], register, pointer+1
        elif instr == 5:
            # out
            out_values = [int(s) for s in str(op % 8)]
            return out_values, register, pointer+1
        elif instr == 6:
            # bdv
            res = int(register['A'] / (2**op))
            register['B'] = res
            return [], register, pointer+1
        elif instr == 7:
            # cdv
            res = int(register['A'] / (2**op))
            register['C'] = res
            return [], register, pointer+1

    pointer = 0
    results = []
    while True:
        if pointer >= len(instruction_op):
            break
        instruction = instruction_op[pointer][0]
        operand = instruction_op[pointer][1]
        res, registers, pointer = exe_instruction(instruction, operand, registers, pointer)
        results = results + res
        pass
    total = str(results).replace(' ', '').replace('[', '').replace(']', '')
    return total


def task_02(inputs):
    total = 0
    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
