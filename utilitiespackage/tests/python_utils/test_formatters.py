from datetime import timedelta, datetime

from utilitiespackage.python_utils.formatters import camel_to_underscore, timesince


def test_camel_to_underscore():
    assert camel_to_underscore("SpamEggsAndBacon") == "spam_eggs_and_bacon"
    assert camel_to_underscore("__SpamANDBacon__") == "__spam_and_bacon__"


def test_timesince():
    now = datetime.now()
    assert timesince(now) == "just now"
    assert timesince(now - timedelta(seconds=3600)) == "1 hour ago"
    assert timesince(now - timedelta(seconds=1)) == "1 second ago"
    assert timesince(now - timedelta(seconds=60)) == "1 minute ago"
    assert timesince(timedelta(seconds=3721)) == "1 hour and 2 minutes ago"
