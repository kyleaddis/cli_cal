import pytest
from cli_cal.cal import Month


def test_answer():
    m = Month(10, 2024)
    print(m.get_weeks())
    assert m.days == 31
    assert m.month_index == 9
    assert m.year == 2024
