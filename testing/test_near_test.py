import pytest


@pytest.mark.parametrize("input1, input2, expected", [
    (1, 2, 3),
    (0.1, 0.2, 0.3),
])
def test_near_test(input1, input2, expected):
    from near_test import add
    answer = add(input1, input2)
    assert answer == pytest.approx(expected)
