from solution import num_deeper, sliding_num_deeper

input_data = """199
200
208
210
200
207
240
269
260
263"""


def test_num_deeper():
    calc_num_deeper = num_deeper(input_data)
    assert calc_num_deeper == 7


def test_sliding_num_deeper():
    calc_sliding_num_deeper = sliding_num_deeper(input_data)
    assert calc_sliding_num_deeper == 5
