import numpy as np
import re
import networkx as nx
import matplotlib.pyplot as plt


def read_input():
    loc = 'aoc_10_input.txt'
    # loc = 'aoc_10_example.txt'
    # loc = 'aoc_10_example_2.txt'
    file = open(loc, 'r')
    content = [[int(d) for d in s.replace('\n', '')] for s in file.readlines()]
    return content


def task_01(inputs):
    # create graph from connected nodes
    G = nx.DiGraph()
    zero_nodes = []
    nine_nodes = []
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            node_name = str(i)+'|'+str(j)
            G.add_node(node_name)
            if inputs[i][j] == 0:
                zero_nodes.append(node_name)
            elif inputs[i][j] == 9:
                nine_nodes.append(node_name)
            n_plus = inputs[i][j] + 1
            n_minus = inputs[i][j] - 1
            # top
            if i != 0:
                if inputs[i-1][j] == n_plus:
                    G.add_edge(node_name, str(i-1)+'|'+str(j))
                if inputs[i-1][j] == n_minus:
                    G.add_edge(str(i-1)+'|'+str(j), node_name)
            # left
            if j != 0:
                if inputs[i][j-1] == n_plus:
                    G.add_edge(node_name, str(i)+'|'+str(j-1))
                if inputs[i][j-1] == n_minus:
                    G.add_edge(str(i)+'|'+str(j-1), node_name)

    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    # plt.show(block=True)

    total = 0
    for zero_n in zero_nodes:
        trails = 0
        for nine_n in nine_nodes:
            # check if path exist
            if nx.has_path(G, zero_n, nine_n):
                trails += 1
        total += trails

    return total


def task_02(inputs):
    # create graph from connected nodes
    G = nx.DiGraph()
    zero_nodes = []
    nine_nodes = []
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            node_name = str(i)+'|'+str(j)
            G.add_node(node_name)
            if inputs[i][j] == 0:
                zero_nodes.append(node_name)
            elif inputs[i][j] == 9:
                nine_nodes.append(node_name)
            n_plus = inputs[i][j] + 1
            n_minus = inputs[i][j] - 1
            # top
            if i != 0:
                if inputs[i-1][j] == n_plus:
                    G.add_edge(node_name, str(i-1)+'|'+str(j))
                if inputs[i-1][j] == n_minus:
                    G.add_edge(str(i-1)+'|'+str(j), node_name)
            # left
            if j != 0:
                if inputs[i][j-1] == n_plus:
                    G.add_edge(node_name, str(i)+'|'+str(j-1))
                if inputs[i][j-1] == n_minus:
                    G.add_edge(str(i)+'|'+str(j-1), node_name)

    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    # plt.show(block=True)

    total = 0
    for zero_n in zero_nodes:
        trails = 0
        for nine_n in nine_nodes:
            # check if path exist
            if nx.has_path(G, zero_n, nine_n):
                # get all possible paths from 0 to 9 for this pair
                all_trails = list(nx.all_simple_paths(G, zero_n, nine_n))
                trails += len(all_trails)
        total += trails

    return total


if __name__ == '__main__':
    inputs = read_input()
    t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass
