#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

HIGHEST_FISH_DAYS = 8
RESET_TO = 6

def simulate_day(fish_map):
    new_fish_map = {num: 0 for num in range(HIGHEST_FISH_DAYS + 1)}
    for at_day in range(HIGHEST_FISH_DAYS + 1):
        number = fish_map[at_day]
        if at_day == 0:
            new_fish_map[HIGHEST_FISH_DAYS] += number
            new_fish_map[RESET_TO] += number
        else:
            new_fish_map[at_day - 1] += number
    return new_fish_map


def simulate_days(fish_map, days):
    for _ in range(days):
        fish_map = simulate_day(fish_map)
    return sum(fish_map.values())

def part_1(input_data, days):
    input_data = input_data.strip()
    total_fish = 0
    fish_map = {num: 0 for num in range(HIGHEST_FISH_DAYS + 1)}
    for fish in input_data.split(","):
        fish_map[int(fish)] += 1
    answer = simulate_days(fish_map, int(days))
    return answer

def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(part_1(input_data, 80))
    print(part_1(input_data, 256))


if __name__ == "__main__":
    main()
