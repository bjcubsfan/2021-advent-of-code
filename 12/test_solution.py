import pytest
from solution import part_1, part_2

input_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input_data_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input_data_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

@pytest.mark.parametrize(
    "input_data, paths",
    [
        (input_data, True),
        (input_data_2, True),
        (input_data_3, True),
    ],
)
def test_part_1(input_data, paths):
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == paths

def test_part_2():
    calc_part_2 = part_2(input_data)
    assert calc_part_2 == 20
