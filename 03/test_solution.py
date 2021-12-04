from solution import power_consumption, oxygen_generator_rating, co2_scrubber_rating

input_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_power_consumption():
    calc_pow = power_consumption(input_data)
    assert calc_pow == 198


def test_oxygen_generator_rating():
    calc_ox = oxygen_generator_rating(input_data)
    assert calc_ox == 23


def test_co2_scrubber_rating():
    calc_co2 = co2_scrubber_rating(input_data)
    assert calc_co2 == 10
