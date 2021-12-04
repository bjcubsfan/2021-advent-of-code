#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint


class Board(object):
    def __init__(self):
        self.rows_and_cols = list()
        self.numbers_uncalled = list()
        self.last_called = None
        self.is_winner = False
        self.win_score = None
        self.total_uncalled = None

    def number_called(self, number):
        self.last_called = number
        if number in set(self.numbers_uncalled):
            self.numbers_uncalled.remove(number)
        new_rcs = list()
        for rc in self.rows_and_cols:
            if number in rc:
                rc.remove(number)
            if len(rc) == 0:
                self.winner()
            new_rcs.append(rc)
        self.rows_and_cols = new_rcs

    def winner(self):
        self.total_uncalled = sum(self.numbers_uncalled)
        self.is_winner = True
        self.win_score = self.total_uncalled * self.last_called

    def win_info(self):
        self.total_uncalled = sum(self.numbers_uncalled)
        print(
            f"winner! sum({self.numbers_uncalled}) = {self.total_uncalled} * {self.last_called} = {self.total_uncalled * self.last_called}"
        )


def simulate(input_data):
    input_data = input_data.strip().split("\n")
    numbers_to_call = input_data[0].split(",")
    numbers_to_call = [int(num) for num in numbers_to_call]
    current_board = None
    boards = list()
    for line in input_data[1:]:
        line = line.strip()
        if not line:
            if current_board:
                for column in columns:
                    current_board.rows_and_cols.append(column)
                boards.append(current_board)
            current_board = Board()
            columns = [[], [], [], [], []]
            continue
        row_numbers = line.split()
        row_numbers = [int(row_number) for row_number in row_numbers]
        for index, number in enumerate(row_numbers):
            columns[index].append(number)
            current_board.numbers_uncalled.append(number)
        current_board.rows_and_cols.append(row_numbers)
    # catch last one
    for column in columns:
        current_board.rows_and_cols.append(column)
    boards.append(current_board)
    first_winner_score = None
    last_winner_score = None
    for num in numbers_to_call:
        for board in set(boards):
            board.number_called(num)
            if board.is_winner:
                if not first_winner_score:
                    first_winner_score = board.win_score
                if len(boards) == 1:
                    last_winner_score = board.win_score
                boards.remove(board)
    return first_winner_score, last_winner_score


def part_1(input_data):
    first_winner_score, last_winner_score = simulate(input_data)
    return first_winner_score


def part_2(input_data):
    first_winner_score, last_winner_score = simulate(input_data)
    return last_winner_score


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    main()
