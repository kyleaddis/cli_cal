import pytest
from cli_cal.cal import Calendar

def test_leap_year():
    y = Calendar(2024)
    y1 = Calendar(2023)
    y2 = Calendar(2000)
    assert y.is_leap_year == True
    assert y1.is_leap_year == False
    assert y2.is_leap_year == True