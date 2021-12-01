import pytest

from solution import real_room, decrypt

rooms = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""


@pytest.mark.parametrize(
    "encrypted_room, is_real_room",
    [
        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
        ("a-b-c-d-e-f-g-h-987[abcde]", True),
        ("not-a-real-room-404[oarel]", True),
        ("totally-real-room-200[decoy]", False),
    ],
)
def test_real_room(encrypted_room, is_real_room):
    is_real, _ = real_room(encrypted_room)
    assert is_real == is_real_room


def test_decrypt():
    assert decrypt("qzmt-zixmtkozy-ivhz-343[checksum]") == "very encrypted name"
