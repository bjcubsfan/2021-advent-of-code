#!/usr/bin/env python

from collections import defaultdict


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


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(power_consumption(input_data))


if __name__ == "__main__":
    main()
