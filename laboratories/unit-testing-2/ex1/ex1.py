import datetime
from unittest.mock import Mock

REAL_DATETIME = datetime.datetime

def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)

def test_year_mock_direct():
    global datetime
    original_datetime = datetime
    datetime = Mock()
    try:
        datetime.datetime.today.return_value = REAL_DATETIME(2024, 1, 1)
        assert is_leap_year() is True

        datetime.datetime.today.return_value = REAL_DATETIME(2023, 1, 1)
        assert is_leap_year() is False
    finally:
        datetime = original_datetime
