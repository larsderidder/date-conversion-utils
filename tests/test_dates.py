"""
Tests for date conversion helpers.
"""

from datetime import datetime

import pytest

from date_conversion_utils import (
    datetime_from_day_of_year,
    is_leap_year,
    year_to_date_range,
)


class TestYearToDateRange:
    """
    Tests for yearly datetime boundaries.
    """

    def test_regular_year(self) -> None:
        """
        Return boundaries for a regular year.
        """
        start, end = year_to_date_range(2015)

        assert start == datetime(2015, 1, 1, 0, 0, 0)
        assert end == datetime(2015, 12, 31, 23, 59, 59, 999999)

    def test_leap_year(self) -> None:
        """
        Return boundaries for a leap year.
        """
        start, end = year_to_date_range(2016)

        assert start == datetime(2016, 1, 1, 0, 0, 0)
        assert end == datetime(2016, 12, 31, 23, 59, 59, 999999)


class TestIsLeapYear:
    """
    Tests for Gregorian leap year rules.
    """

    def test_regular_year(self) -> None:
        """
        Return false for a regular year.
        """
        assert is_leap_year(2015) is False

    def test_divisible_by_4(self) -> None:
        """
        Return true for years divisible by four.
        """
        assert is_leap_year(2016) is True

    def test_century_not_leap(self) -> None:
        """
        Return false for most century years.
        """
        assert is_leap_year(1900) is False

    def test_400_year_leap(self) -> None:
        """
        Return true for years divisible by four hundred.
        """
        assert is_leap_year(2000) is True


class TestDatetimeFromDayOfYear:
    """
    Tests for converting day numbers to datetimes.
    """

    def test_first_day(self) -> None:
        """
        Convert the first day of a year.
        """
        result = datetime_from_day_of_year(2015, 1)

        assert result == datetime(2015, 1, 1)

    def test_last_day(self) -> None:
        """
        Convert the last day of a regular year.
        """
        result = datetime_from_day_of_year(2015, 365)

        assert result == datetime(2015, 12, 31)

    def test_leap_year_day_366(self) -> None:
        """
        Convert the last day of a leap year.
        """
        result = datetime_from_day_of_year(2016, 366)

        assert result == datetime(2016, 12, 31)

    def test_rejects_zero(self) -> None:
        """
        Reject day zero.
        """
        with pytest.raises(ValueError, match="at least 1"):
            datetime_from_day_of_year(2016, 0)

    def test_rejects_day_past_year_end(self) -> None:
        """
        Reject days beyond the selected year.
        """
        with pytest.raises(ValueError, match="at most 365"):
            datetime_from_day_of_year(2015, 366)
