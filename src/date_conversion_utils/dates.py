"""
Date and year conversion helpers.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta


def year_to_date_range(year: int) -> tuple[datetime, datetime]:
    """
    Return the first and last datetime in a calendar year.
    """
    start = datetime.combine(date(year, 1, 1), time.min)
    end = datetime.combine(date(year, 12, 31), time.max)
    return start, end


def is_leap_year(year: int) -> bool:
    """
    Return whether a year is a leap year in the Gregorian calendar.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def datetime_from_day_of_year(year: int, day: int) -> datetime:
    """
    Convert a one-based day of year to a datetime at midnight.
    """
    if day < 1:
        raise ValueError("day must be at least 1")
    max_day = 366 if is_leap_year(year) else 365
    if day > max_day:
        raise ValueError(f"day must be at most {max_day} for {year}")
    return datetime.combine(date(year, 1, 1) + timedelta(days=day - 1), time.min)
