#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

def calc_fuel_cost(positions, test_position):
    fuel_cost = 0
    for position in positions:
        fuel_cost += abs(position - test_position)
    return fuel_cost

def part_1(input_data):
    input_data = input_data.strip()
    answer = None
    positions = [int(number) for number in input_data.split(",")]
    least_fuel = None
    best_position = None
    for test_position in range(max(positions)):
        fuel_cost = calc_fuel_cost(positions, test_position)
        if not least_fuel or fuel_cost < least_fuel:
            best_position = test_position
            least_fuel = fuel_cost
    print(f"Found least fuel of {least_fuel} used at {best_position}.")
    return least_fuel

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
