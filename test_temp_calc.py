import pytest


@pytest.mark.parametrize("my_input, expected", [
    ([96, 96.5, 101.7, 98.7], True),
    ([96, 96.5, 99.0, 98.7], False)])
def test_detect_fever(my_input, expected):
    from temp_calc import detect_fever
    answer = detect_fever(my_input)
    assert answer == expected
