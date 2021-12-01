#!/usr/bin/env python


def special_sum(digits):
    sum = 0
    for first, second in zip(digits, digits[1:]):
        first = int(first)
        second = int(second)
        if first == second:
            sum += first
    if int(digits[-1]) == int(digits[0]):
        sum += int(digits[-1])
    return sum


def half_sum(digits):
    sum = 0
    assert len(digits) % 2 == 0
    halfway = int(len(digits) / 2)
    for index, digit in enumerate(digits):
        compare_index = (halfway + index) % len(digits)
        if int(digit) == int(digits[compare_index]):
            sum += int(digit)
    return sum


def main():
    with open("input") as input_data:
        for line in input_data:
            print(special_sum(line.strip()))
            print(half_sum(line.strip()))


if __name__ == "__main__":
    main()
