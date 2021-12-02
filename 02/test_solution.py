from solution import advanced_position_multiplied, position_multiplied

input_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_position_multiplied():
    calc_pos_mult = position_multiplied(input_data)
    assert calc_pos_mult == 150


def test_advanced_position_multiplied():
    calc_pos_mult = advanced_position_multiplied(input_data)
    assert calc_pos_mult == 900
