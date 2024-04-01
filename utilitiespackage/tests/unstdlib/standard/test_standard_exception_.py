from utilitiespackage.unstdlib.standard.exception_ import convert_exception


def test_standard_exception_convert_exception():
    class FooError(Exception):
        pass

    class BarError(Exception):
        def __init__(self, message):
            self.message = message

    @convert_exception(FooError, BarError, message="bar")
    def throw_foo():
        raise FooError("foo")

    try:
        throw_foo()
    except BarError as e:
        assert e.message == "bar"
