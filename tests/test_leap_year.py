import pytest
from cli_cal.cal import Calendar

def test_leap_year():
    y = Calendar(2024)
    y1 = Calendar(2023)
    assert y.is_leap_year == True
    assert y1.is_leap_year == False