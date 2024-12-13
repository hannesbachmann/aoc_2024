import numpy as np
import re
import cv2
import pandas as pd
from skimage.measure import label, regionprops, regionprops_table


def read_input():
    loc = 'aoc_12_input.txt'
    loc = 'aoc_12_example.txt'
    # loc = 'aoc_12_example_2.txt'
    # loc = 'aoc_12_example_3.txt'
    file = open(loc, 'r')
    content = np.asarray([np.asarray([d for d in s.replace('\n', '')]) for s in file.readlines()])
    return content


def task_01(inputs):
    # replace each alphabetical number with a numeric one (to interpret input as an image)
    all_chars = np.unique(inputs)
    char_num_mapper = {all_chars[c]: c+1 for c in range(all_chars.shape[0])}
    x, y = inputs.shape
    num_inputs = np.zeros(shape=(x+2, y+2), dtype='uint32')
    for i in range(1, len(inputs)+1):
        for j in range(1, len(inputs[i-1])+1):
            num_inputs[i][j] = char_num_mapper[inputs[i-1][j-1]]
    # find connected components (with stats) and get area of each component
    label_im = label(num_inputs, connectivity=1)    # 1 connectivity to use only vertical and horizontal neighbors
    regions = regionprops(label_im)
    # map area to label
    label_area_mapper = {r.label: r.area for r in regions}
    # go through the unique numbers in the components
    component_neighbors_mapper = {r.label: 0 for r in regions if r.label != 0}
    for l in component_neighbors_mapper.keys():
        # calculate perimeter (surrounding pixels in the 4-neighborhood)
        # go through all pixels to search for neighbors (4-neighborhood)
        check_neighbor_mask = np.zeros(shape=label_im.shape)
        perim = 0
        for i in range(label_im.shape[0]):
            for j in range(label_im.shape[1]):
                if label_im[i][j] != l:
                    if i > 0:
                        # top
                        if label_im[i-1][j] == l:
                            perim += 1
                            check_neighbor_mask[i][j] = 1
                    if i < label_im.shape[0] - 1:
                        # bottom
                        if label_im[i+1][j] == l:
                            perim += 1
                            check_neighbor_mask[i][j] = 1
                    if j > 0:
                        # left
                        if label_im[i][j-1] == l:
                            perim += 1
                            check_neighbor_mask[i][j] = 1
                    if j < label_im.shape[1] - 1:
                        # right
                        if label_im[i][j+1] == l:
                            perim += 1
                            check_neighbor_mask[i][j] = 1
        component_neighbors_mapper[l] = perim
    # all_labels = np.unique(labels)
    # cv2.imshow('w', cv2.resize(labels.astype('uint8'), dsize=(labels.shape[0] * 100, labels.shape[1] * 100)) * 50)
    # cv2.waitKey()

    # calculate score by multiplying area with perimeter for each component
    total = sum([label_area_mapper[r.label]*component_neighbors_mapper[r.label] for r in regions if r.label != 0])
    return total


def task_02(inputs):
    # replace each alphabetical number with a numeric one (to interpret input as an image)
    all_chars = np.unique(inputs)
    char_num_mapper = {all_chars[c]: c + 1 for c in range(all_chars.shape[0])}
    x, y = inputs.shape
    num_inputs = np.zeros(shape=(x + 2, y + 2), dtype='uint32')
    for i in range(1, len(inputs) + 1):
        for j in range(1, len(inputs[i - 1]) + 1):
            num_inputs[i][j] = char_num_mapper[inputs[i - 1][j - 1]]
    # find connected components (with stats) and get area of each component
    label_im = label(num_inputs, connectivity=1)  # 1 connectivity to use only vertical and horizontal neighbors
    regions = regionprops(label_im)
    # map area to label
    label_area_mapper = {r.label: r.area for r in regions}
    # go through the unique numbers in the components
    component_neighbors_mapper = {r.label: 0 for r in regions if r.label != 0}
    for l in component_neighbors_mapper.keys():
        # calculate perimeter (surrounding pixels in the 4-neighborhood)
        # go through all pixels to search for neighbors (4-neighborhood)
        check_neighbor_mask = np.zeros(shape=label_im.shape, dtype='uint8')
        perim = 0
        for i in range(label_im.shape[0]):
            for j in range(label_im.shape[1]):
                if label_im[i][j] != l:
                    if i > 0:
                        # top
                        if label_im[i - 1][j] == l:
                            perim += 1
                            check_neighbor_mask[i][j] += 1
                    if i < label_im.shape[0] - 1:
                        # bottom
                        if label_im[i + 1][j] == l:
                            perim += 1
                            check_neighbor_mask[i][j] += 1
                    if j > 0:
                        # left
                        if label_im[i][j - 1] == l:
                            perim += 1
                            check_neighbor_mask[i][j] += 1
                    if j < label_im.shape[1] - 1:
                        # right
                        if label_im[i][j + 1] == l:
                            perim += 1
                            check_neighbor_mask[i][j] += 1
        component_neighbors_mapper[l] = perim
        cv2.imshow('win', cv2.resize(check_neighbor_mask, dsize=(check_neighbor_mask.shape[0] * 8, check_neighbor_mask.shape[1] * 8)) * 32)
        cv2.waitKey()
    # all_labels = np.unique(labels)
    # cv2.imshow('w', cv2.resize(labels.astype('uint8'), dsize=(labels.shape[0] * 100, labels.shape[1] * 100)) * 50)
    # cv2.waitKey()

    # calculate score by multiplying area with perimeter for each component
    total = sum([label_area_mapper[r.label] * component_neighbors_mapper[r.label] for r in regions if r.label != 0])
    return total


if __name__ == '__main__':
    inputs = read_input()
    # t1_solution = task_01(inputs)
    t2_solution = task_02(inputs)
    pass

# 0111100
# 1++++10
# 1+33+10
# 1+++200
# 0111000
