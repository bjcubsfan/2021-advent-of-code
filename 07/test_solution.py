from solution import part_1, part_2

input_data = """16,1,2,0,4,2,7,1,2,14"""


def test_part_1():
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == 37

def test_part_2():
    calc_part_2 = part_2(input_data)
    assert calc_part_2 == 168
