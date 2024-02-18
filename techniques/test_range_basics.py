from range_basics import basic_range


def test_basic_range() -> None:
    expected = [1, 2, 3, 4, 5]
    assert expected == basic_range(1, 6)
