#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint


def power_consumption(input_data):
    input_data = input_data.strip()
    power = 0
    tallies = defaultdict()
    first = True
    for line in input_data.split("\n"):
        line = line.strip()
        if not line:
            continue
        if first:
            binary_length = len(line)
            for position in range(binary_length):
                tallies[position] = defaultdict(int)
            first = False
        for position, value in enumerate(line):
            value = int(value.strip())
            tallies[position][value] += 1
    min_binary = []
    max_binary = []
    for position in range(binary_length):
        zeroes = tallies[position][0]
        ones = tallies[position][1]
        if zeroes > ones:
            min_binary.append("1")
            max_binary.append("0")
        elif ones > zeroes:
            min_binary.append("0")
            max_binary.append("1")
        else:
            raise Error
    min_num = int(f"0b{''.join(min_binary)}", 2)
    max_num = int(f"0b{''.join(max_binary)}", 2)
    return min_num * max_num


def most_common_in_position(numbers, bit_to_check):
    tallies = defaultdict(int)
    for number in numbers:
        tallies[number[bit_to_check]] += 1
    if tallies["0"] > tallies["1"]:
        return ("0", "1")
    elif tallies["0"] < tallies["1"]:
        return ("1", "0")
    else:
        # Ties defined in problem
        return ("1", "0")


def pare_list(numbers, bit_to_check, pare_by):
    most_common, least_common = most_common_in_position(numbers, bit_to_check)
    # pprint(numbers)
    # print(
    #     f"for {bit_to_check}, most common: {most_common}, least_common: {least_common}"
    # )
    # print(60 * "#")
    if pare_by == "most":
        return [number for number in numbers if number[bit_to_check] == most_common]
    elif pare_by == "least":
        return [number for number in numbers if number[bit_to_check] == least_common]


def numbers_and_length(input_data):
    numbers = list()
    first = True
    for line in input_data.split("\n"):
        line = line.strip()
        if not line:
            continue
        if first:
            binary_length = len(line)
            first = False
        numbers.append(line)
    return numbers, binary_length


def rating(input_data, pare_by):
    first = True
    numbers, length = numbers_and_length(input_data)
    for bit_to_check in range(length):
        numbers = pare_list(numbers, bit_to_check, pare_by)
        # print(f"paring by {pare_by}")
        # pprint(numbers)
        # print(60 * "*")
        if len(numbers) == 1:
            return int(numbers[0], 2)
    print("never got to one.")


def co2_scrubber_rating(input_data):
    return rating(input_data, "least")


def oxygen_generator_rating(input_data):
    return rating(input_data, "most")


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(power_consumption(input_data))
    co2 = co2_scrubber_rating(input_data)
    o2 = oxygen_generator_rating(input_data)
    print(f"co2: {co2}, o2: {o2}, total: {co2 * o2}")


if __name__ == "__main__":
    main()
