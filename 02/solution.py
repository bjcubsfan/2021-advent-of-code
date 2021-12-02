#!/usr/bin/env python


def advanced_update_position(aim, horizontial, depth, instruction):
    token, number = instruction.split()
    number = int(number.strip())
    if token == "forward":
        horizontial += number
        depth += aim * number
    elif token == "up":
        aim -= number
    elif token == "down":
        aim += number
    return aim, horizontial, depth


def update_position(horizontial, depth, instruction):
    token, number = instruction.split()
    number = int(number.strip())
    if token == "forward":
        horizontial += number
    elif token == "up":
        depth -= number
    elif token == "down":
        depth += number
    return horizontial, depth


def position_multiplied(input_data):
    horizontal = 0
    depth = 0
    input_data = input_data.strip()
    for line in input_data.split("\n"):
        horizontal, depth = update_position(horizontal, depth, line)
    return horizontal * depth


def advanced_position_multiplied(input_data):
    aim = 0
    horizontal = 0
    depth = 0
    input_data = input_data.strip()
    for line in input_data.split("\n"):
        aim, horizontal, depth = advanced_update_position(aim, horizontal, depth, line)
    return horizontal * depth


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(position_multiplied(input_data))
    print(advanced_position_multiplied(input_data))


if __name__ == "__main__":
    main()
