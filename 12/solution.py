#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

class Cave(object):
    def __init__(self, input_data):
        self.connections = defaultdict(set)
        found_paths = set()
        for line in input_data.split("\n"):
            line = line.strip()
            first, second = line.split("-")
            self.connections[first].add(second)
            self.connections[second].add(first)


    def find_paths(self):
        for first_step in self.connections['start']:
            self.recourse_through()

def part_1(input_data):
    input_data = input_data.strip()
    answer = None
    cave = Cave(input_data)
    import IPython; IPython.embed()
    return answer

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
