from blood_calc import hdl_eval
import pytest


@pytest.mark.parametrize("HDL_value, expected", [  # <-- decorator
    (65, "Normal"),
    (45, "Borderline low"),
    (30, "Low")])
def test_hdl_analysis(HDL_value, expected):
    answer = hdl_eval(HDL_value)
    assert answer == expected
