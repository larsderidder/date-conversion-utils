# date-conversion-utils

Small helpers for converting years and day-of-year values into `datetime` objects.

## Install

Install from source:

```bash
git clone https://github.com/larsderidder/date-conversion-utils.git
cd date-conversion-utils
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install .
```

## Usage

```python
from date_conversion_utils import datetime_from_day_of_year, is_leap_year, year_to_date_range

start, end = year_to_date_range(2016)
# datetime(2016, 1, 1, 0, 0), datetime(2016, 12, 31, 23, 59, 59, 999999)

is_leap_year(2016)  # True

datetime_from_day_of_year(2016, 60)  # datetime(2016, 2, 29)
```

`datetime_from_day_of_year` accepts one-based day numbers and raises `ValueError`
when the day is outside the selected year.

## Development

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
```
