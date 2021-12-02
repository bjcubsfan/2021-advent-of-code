#!/usr/bin/env python

from collections import deque


def num_deeper(input_data):
    running_total = 0
    previous_entry = None
    input_data = input_data.strip()
    for line in input_data.split("\n"):
        line = line.strip()
        current_entry = int(line)
        if previous_entry is None:
            previous_entry = current_entry
            continue
        elif current_entry > previous_entry:
            running_total += 1
            previous_entry = current_entry
        else:
            previous_entry = current_entry
    return running_total


def sliding_num_deeper(input_data):
    running_total = 0
    input_data = input_data.strip()
    window = deque(maxlen=4)
    for line in input_data.split("\n"):
        current_number = int(line.strip())
        window.append(current_number)
        if len(window) < 4:
            continue
        previous_sum = sum(list(window)[0:3])
        current_sum = sum(list(window)[1:4])
        if current_sum > previous_sum:
            running_total += 1
    return running_total


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(num_deeper(input_data))
    print(sliding_num_deeper(input_data))


if __name__ == "__main__":
    main()
