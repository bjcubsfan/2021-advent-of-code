#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint


def part_1_fuel(positions, test_position):
    fuel_cost = 0
    for position in positions:
        fuel_cost += abs(position - test_position)
    return fuel_cost


def part_2_distance_cost(distance):
    cost = 0
    extra_cost = 0
    for _ in range(1, distance + 1):
        cost += 1 + extra_cost
        extra_cost += 1
    return cost


def part_2_fuel(positions, test_position):
    fuel_cost = 0
    for position in positions:
        fuel_cost += part_2_distance_cost(abs(position - test_position))
    return fuel_cost


def simulate(input_data, part):
    input_data = input_data.strip()
    answer = None
    positions = [int(number) for number in input_data.split(",")]
    least_fuel = None
    best_position = None
    if part == 1:
        calculate_fuel_cost = part_1_fuel
    elif part == 2:
        calculate_fuel_cost = part_2_fuel
    print(f"Need to solve {max(positions)} positions")
    for test_position in range(max(positions)):
        if test_position % 10 == 0:
            print(
                f"Solving position number {test_position}, best position is {best_position} with cost of {least_fuel}"
            )
        fuel_cost = calculate_fuel_cost(positions, test_position)
        if not least_fuel or fuel_cost < least_fuel:
            best_position = test_position
            least_fuel = fuel_cost
    print(f"Found least fuel of {least_fuel} used at {best_position}.")
    return least_fuel


def part_1(input_data):
    return simulate(input_data, 1)


def part_2(input_data):
    return simulate(input_data, 2)


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    main()
