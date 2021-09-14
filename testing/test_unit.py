import pytest


@pytest.mark.parametrize("my_input_1, my_input_2, my_input_3, expected", [
    ((1, 2), (2, 4), 3, 6),
    ((0, 4), (4, 10), 2, 7)])
def test_xy_calc(my_input_1, my_input_2, my_input_3, expected):
    from x_to_y import get_new_y
    answer = get_new_y(my_input_1, my_input_2, my_input_3)
    assert answer == expected


@pytest.mark.parametrize("num, expected", [
    (str(5), True),
    ("5c", False),
    (float(5), True),
    (int(5), True),
    ([5], False)])
def test_number(num, expected):
    from x_to_y import is_numeric
    answer = is_numeric(num)
    assert answer == expected
