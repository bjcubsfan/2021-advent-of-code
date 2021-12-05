#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint
import numpy as np

def coordinates(line):
    first, second = line.split(" -> ")
    x1, y1 = first.split(",")
    x2, y2 = second.split(",")
    return int(x1), int(y1), int(x2), int(y2)

def mark_grid(horizontal_lines, vertical_lines, max_x, max_y):
    grid = np.zeros((max_x + 1, max_y + 1))
    for line in horizontal_lines:
        c1, c2 = line
        x = c1[0]
        ys = [c1[1], c2[1]]
        for y in range(min(ys), max(ys) + 1):
            grid[x, y] += 1
    for line in vertical_lines:
        c1, c2 = line
        y = c1[1]
        xs = [c1[0], c2[0]]
        for x in range(min(xs), max(xs) + 1):
            grid[x, y] += 1
    return grid

def part_1(input_data):
    input_data = input_data.strip()
    answer = None
    x_values = []
    y_values = []
    horizontal_lines = []
    vertical_lines = []
    for line in input_data.split("\n"):
        line = line.strip()
        x1, y1, x2, y2 = coordinates(line)
        x_values.append(x1)
        x_values.append(x2)
        y_values.append(y1)
        y_values.append(y2)
        if x1 == x2:
            horizontal_lines.append(((x1, y1), (x2, y2)))
        elif y1 == y2:
            vertical_lines.append(((x1, y1), (x2, y2)))
    marked_grid = mark_grid(
            horizontal_lines, vertical_lines, max(x_values), max(y_values)
            )
    return np.sum(marked_grid >= 2)

def part_2(input_data):
    input_data = input_data.strip()
    answer = None
    for line in input_data.split("\n"):
        line = line.strip()
    return answer

def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    main()
