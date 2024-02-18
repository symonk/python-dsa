from range_basics import basic_range


def test_basic_range() -> None:
    expected = [1, 2, 3, 4, 5]
    assert expected == basic_range(1, 6)


def test_range_can_be_negative() -> None:
    expected = [-30, -20, -10]
    assert expected == basic_range(-30, -9, 10)
