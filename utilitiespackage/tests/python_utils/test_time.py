from datetime import timedelta, datetime, date

from utilitiespackage.python_utils.time import timedelta_to_seconds, format_time


def test_timedelta_to_seconds():
    assert "%d" % timedelta_to_seconds(timedelta(days=1)) == "86400"
    assert "%d" % timedelta_to_seconds(timedelta(seconds=1)) == "1"
    assert "%.6f" % timedelta_to_seconds(timedelta(microseconds=1)) == "0.000001"


def test_format_time():
    assert format_time("1") == "0:00:01"
    assert format_time(1.234) == "0:00:01"
    assert format_time(date(2000, 1, 2)) == "2000-01-02"
    assert format_time(datetime(2000, 1, 2, 3, 4, 5, 6)) == "2000-01-02 03:04:05"
    assert format_time(timedelta(seconds=3661)) == "1:01:01"
    assert format_time(None) == "--:--:--"
