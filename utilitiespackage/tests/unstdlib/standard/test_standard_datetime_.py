import calendar
import datetime

import pytz

from utilitiespackage.unstdlib.standard.datetime_ import (
    iterate_date_values,
    isoformat_as_datetime,
    truncate_datetime,
    to_timezone,
    now,
    datetime_from_timestamp,
    timestamp_from_datetime,
    _UTC,
)


def test_standard_datetime_iterate_date_values():
    assert list(iterate_date_values([(datetime.date(2011, 1, 1), 1), (datetime.date(2011, 1, 4), 2)])) == [1, 0, 0, 2]
    assert list(iterate_date_values([(datetime.date(2011, 1, 1), 1), (datetime.date(2011, 1, 4), 2)], start_date=datetime.date(2011, 1, 2))) == [
        0,
        0,
        2,
    ]


def test_standard_datetime_isoformat_as_datetime():
    dt = datetime.datetime(2010, 8, 4, 9, 33, 9)
    assert isoformat_as_datetime("%s" % (dt.isoformat())) == datetime.datetime(2010, 8, 4, 9, 33, 9)


def test_standard_datetime_truncate_datetime():
    t = datetime.datetime(2000, 1, 2, 3, 4, 5, 6000)
    assert truncate_datetime(t, "day").isoformat() == "2000-01-02T00:00:00"
    assert truncate_datetime(t, "minute").isoformat() == "2000-01-02T03:04:00"


def test_standard_datetime_to_timezone():
    t = datetime.datetime(2000, 1, 2, 3, 4, 5, 6000)
    assert to_timezone(t, pytz.timezone("US/Eastern"))


def test_standard_datetime_now():
    now()
    now(timezone=pytz.timezone("US/Eastern"))


def test_standard_datetime_datetime_from_timestamp():
    assert datetime_from_timestamp(1234.5) == datetime.datetime(1970, 1, 1, 0, 20, 34, 500000)


def test_standard_datetime_timestamp_from_datetime():
    assert timestamp_from_datetime(datetime.datetime(1970, 1, 1, 0, 20, 34, 500000)) == 1234.5


def test_standard_datetime_utc_class():
    t = datetime.datetime(2000, 1, 2, 3, 4, 5, 6000)
    utc = _UTC()
    assert utc.__repr__() == "<UTC>"
    assert utc.utcoffset(t) == datetime.timedelta(0)
    assert utc.tzname(t) == "UTC"
    assert utc.dst(t) == datetime.timedelta(0)
