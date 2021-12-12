#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

def simulate_fish(value, days):
    return value + days

def part_1(input_data, days):
    input_data = input_data.strip()
    answer = None
    total_fish = 0
    for fish in input_data.split(","):
        final_fish = simulate_fish(int(fish), days)
        total_fish += final_fish
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
    print(part_1(input_data, 3))
    print(part_2(input_data))


if __name__ == "__main__":
    main()
