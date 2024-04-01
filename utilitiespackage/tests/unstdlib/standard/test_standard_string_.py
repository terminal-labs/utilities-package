import string

from utilitiespackage.unstdlib.standard.string_ import (
    r,
    random_string,
    number_to_string,
    string_to_number,
    bytes_to_number,
    number_to_bytes,
    to_str,
    to_unicode,
    to_int,
    to_float,
    format_int,
    dollars_to_cents,
    slugify,
)


def test_random_string():
    assert len(random_string()) == 6
    assert len(random_string(length=10)) == 10


def test_number_to_string():
    assert number_to_string(12345678, "01") == "101111000110000101001110"
    assert number_to_string(12345678, "ab") == "babbbbaaabbaaaababaabbba"
    assert number_to_string(12345678, string.ascii_letters + string.digits) == "ZXP0"
    assert (
        number_to_string(12345, ["zero ", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "])
        == "one two three four five "
    )


def test_string_to_number():
    assert string_to_number("101111000110000101001110", "01") == 12345678
    assert string_to_number("babbbbaaabbaaaababaabbba", "ab") == 12345678
    assert string_to_number("ZXP0", string.ascii_letters + string.digits) == 12345678


def test_bytes_to_number():
    assert bytes_to_number(b"*") == 42
    assert bytes_to_number(b"\xff") == 255


def test_number_to_bytes():
    assert number_to_bytes(42) == b"*"
    assert number_to_bytes(255) == b"\xff"


def test_to_str():
    some_str = b"\xff"
    some_unicode = u"\u1234"
    some_exception = Exception(u"Error: " + some_unicode)
    r(to_str(some_str))
    r(to_str(some_unicode))
    r(to_str(some_exception))
    r(to_str([42]))


def test_to_unicode():
    assert to_unicode(b"\xe1\x88\xb4") == b"\xe1\x88\xb4"
    assert to_unicode(to_str(u"\u1234")) == b"\xe1\x88\xb4"


def test_to_int():
    assert to_int("1") == 1
    assert to_int(1) == 1
    assert to_int("") == 0
    assert to_int(None) == 0
    assert to_int(0, default="Empty") == 0
    assert to_int(None, default="Empty") == "Empty"


def test_to_float():
    assert to_float("1.5") == 1.5
    assert to_float(1) == 1.0
    assert to_float("") == 0.0
    assert to_float("nan") == 0.0
    assert to_float("inf") == 0.0
    assert to_float("-inf", allow_nan=True) == float("-inf")
    assert to_float(None) == 0.0
    assert to_float(0, default="Empty") == 0.0
    assert to_float(None, default="Empty") == "Empty"


def test_format_int():
    assert format_int(1000) == "1,000"
    assert format_int(1, u"{} day") == "1 day"
    assert format_int(2, u"{} day") == "2 days"


def test_dollars_to_cents():
    # assert dollars_to_cents("$1") == 100
    assert dollars_to_cents("1") == 100
    assert dollars_to_cents(1) == 100
    assert dollars_to_cents("1e2") == 10000
    # assert dollars_to_cents("-1$", allow_negative=True) == -100
    # assert dollars_to_cents("1 dollar") == 100


def test_slugify():
    assert slugify("test") == "test"
    assert slugify("next test") == "next-test"
    assert slugify("more numbers 123456789") == "more-numbers-123456789"
