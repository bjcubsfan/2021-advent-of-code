#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint


def part_1(input_data):
    """1, 4, 7, 8 use a unique number of segments"""
    input_data = input_data.strip()
    answer = 0
    for line in input_data.split("\n"):
        line = line.strip()
        patterns, outputs = line.split("|")
        outputs = outputs.strip()
        for output in outputs.split():
            if (
                len(output) == 2  # 1
                or len(output) == 4  # 4
                or len(output) == 3  # 7
                or len(output) == 7  # 8
            ):
                answer += 1
    return answer


def decode(patterns):
    """
    I know 9 is the 6 segment with both c & f, so I know 9
        and I know the missing one there is e
    I know 6 is the only 6 segment without c so I know 6 & c
    I know f since 1 has c & f
    I know a since c & f leave only a in 7
    I know b by elemination in 4
    I know g as it's all that's left
    5 has abdfg
    2 has acdeg
    """
    # print("*" * 60)
    patterns = [set(pattern) for pattern in patterns]
    by_digit = dict()
    by_segment = dict()
    for pattern in patterns:
        if len(pattern) == 2:  # 1
            by_digit[1] = pattern
        elif len(pattern) == 4:  # 4
            by_digit[4] = pattern
        elif len(pattern) == 3:  # 7
            by_digit[7] = pattern
        elif len(pattern) == 7:  # 8
            by_digit[8] = pattern
    # I know 1 & 7, the uncommon between them is a so:
    by_segment["a"] = by_digit[7] - by_digit[1]
    # I know 1, so those are c & f
    orig_cf = by_digit[1]
    # I know 3 is only 5 segment with c & f, so I know d (3)
    for pattern in patterns:
        if len(pattern) == 5:
            if len(orig_cf & pattern) == 2:
                by_digit[3] = pattern
    # I know b is is only segment in 4 but not 3
    by_segment["b"] = by_digit[4] - by_digit[3]
    # I know 6 b/c it's the only 6 segment without orig_cf
    for pattern in patterns:
        if len(pattern) == 6:
            if len(orig_cf & pattern) != 2:
                by_digit[6] = pattern
                # print(f"got 6 as {pattern}")
    # I know c b/c it's the only one not in 6
    by_segment["c"] = by_digit[8] - by_digit[6]
    # I know 5 b/c it's the only 5 segment w/o c
    for pattern in patterns:
        if len(pattern) == 5:
            if len(pattern & by_segment["c"]) == 0:
                by_digit[5] = pattern
    # I know 2 b/c it's the only 5 segment left
    for pattern in patterns:
        if len(pattern) == 5:
            if by_digit[3] != pattern and by_digit[5] != pattern:
                by_digit[2] = pattern
    # I know ie is segment from 2 - 3
    by_segment["e"] = by_digit[2] - by_digit[3]
    # I know f is 1 - c
    by_segment["f"] = by_digit[1] - by_segment["c"]
    # I know 9 b/c it's the 6 segment without e
    for pattern in patterns:
        if len(pattern) == 6:
            if len(by_segment["e"] & pattern) == 0:
                by_digit[9] = pattern
                # print(f"got 9 as {pattern}")
    # I know 9 is the last 6 segment
    for pattern in patterns:
        if len(pattern) == 6:
            if pattern != by_digit[9] and pattern != by_digit[6]:
                by_digit[0] = pattern
                # print(f"got 0 as {pattern}")
    if len(by_digit) != 10:
        import IPython

        IPython.embed()
    decoder = dict()
    for digit in sorted(by_digit):
        pattern = by_digit[digit]
        decoder["".join(sorted(pattern))] = str(digit)
    # print()
    return decoder


#   segments I know  numbers I know
#   a X            | 0        |
#   b X            | 1 X      |
#   c X            | 2        |
#   d              | 3 X      |
#   e X            | 4 X      |
#   f X            | 5 X      |
#   g              | 6        |
#                  | 7 X      |
#                  | 8 X      |
#                  | 9        |


def part_2(input_data):
    """1, 4, 7, 8 use a unique number of segments

      num 0 lights 6 segments
    X num 1 lights 2 segments
      num 2 lights 5 segments *****
    X num 3 lights 5 segments *****
    X num 4 lights 4 segments
      num 5 lights 5 segments *****
      num 6 lights 6 segments
    X num 7 lights 3 segments
    X num 8 lights 7 segments
      num 9 lights 6 segments

    segments I know  numbers I know
    a x            | 0 x
    b x            | 1 x
    c x            | 2 x
    d x            | 3 x
    e x            | 4 x
    f x            | 5 x
    g              | 6 x
                   | 7 x
                   | 8 x
                   | 9 x

    I know 1 & 7, the uncommon between them is a
    I know 1, so those are c & f
    I know 3 is only 5 segment with c & f, so I know d (3)
    I know 0 is the 6 segment without d, so I know 0
    I know 9 is the 6 segment with both c & f, so I know 9
        and I know the missing one there is e
    I know 6 is the only 6 segment without c so I know 6 & c
    I know f since 1 has c & f
    I know a since c & f leave only a in 7
    I know b by elemination in 4
    I know g as it's all that's left
    5 has abdfg
    2 has acdeg
    """
    input_data = input_data.strip()
    total = 0
    for line in input_data.split("\n"):
        line = line.strip()
        patterns, outputs = line.split("|")
        patterns = patterns.strip()
        patterns = patterns.split()
        patterns = [sorted(pattern) for pattern in patterns]
        outputs = outputs.strip()
        outputs = outputs.split()
        outputs = [sorted(output) for output in outputs]
        decoder = decode(patterns)
        try:
            decoded = [decoder["".join(output)] for output in outputs]
        except KeyError:
            import IPython

            IPython.embed()
        total += int("".join(decoded))
    return total


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    main()
