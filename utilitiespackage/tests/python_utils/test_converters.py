import re

from utilitiespackage.python_utils.converters import to_int, to_float, to_unicode, to_str, scale_1024


def test_to_int():
    assert to_int("abc") == 0
    assert to_int("1") == 1
    assert to_int("abc123abc", regexp="(\d+)") == 123
    assert to_int("abc123abc456", regexp=True) == 123
    assert to_int("123abc", regexp=re.compile("(\d+)")) == 123


def test_to_float():
    assert "%.2f" % to_float("abc") == "0.00"
    assert "%.2f" % to_float("abc", regexp="(\d+)") == "0.00"
    assert "%.2f" % to_float("abc123.456", regexp=re.compile("(\d+\.\d+)")) == "123.46"
    assert "%.2f" % to_float("abc123", regexp=True) == "123.00"


def test_to_unicode():
    class Foo(object):
        __str__ = lambda s: u"a"

    assert to_unicode(Foo()) == "a"
    assert to_unicode(b"a") == "a"


def test_to_str():
    class Foo(object):
        __str__ = lambda s: u"a"

    assert to_str(Foo()) == b"a"
    assert to_str("a") == b"a"
    assert to_str(b"a") == b"a"


def test_scale_1024():
    assert scale_1024(310, 3) == (310.0, 0)
    assert scale_1024(-1, 2) == (-1, 0)
