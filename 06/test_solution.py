import pytest
from solution import part_1

input_data = """3,4,3,1,2"""

@pytest.mark.parametrize(
    "days, expected",
    [
        (18, 26),
        (80, 5934),
        (256, 26984457539),
    ],
)
def test_part_1(days, expected):
    calc_part_1 = part_1(input_data, days)
    assert calc_part_1 == expected

