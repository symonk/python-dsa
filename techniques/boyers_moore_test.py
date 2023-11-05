from boyers_moore import boyers_moore


def test_boyers_moore():
    assert boyers_moore([3, 3, 3, 2, 1]) == 3
    assert boyers_moore([1]) == 1
