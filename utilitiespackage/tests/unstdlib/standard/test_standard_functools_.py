import warnings

from utilitiespackage.unstdlib.standard.collections_ import RecentlyUsedContainer
from utilitiespackage.unstdlib.standard.functools_ import assert_hashable, memoized, memoized_method, deprecated


def test_standard_functools_assert_hashable():
    assert_hashable(1, "foo", bar="baz")


def test_standard_functools_memoized():
    @memoized
    def foo(bar):
        return "Not cached."

    assert foo(1) == "Not cached."
    foo(2)


def test_standard_functools_memoized_method():
    class Foo(object):
        @memoized_method(cache_factory=lambda: RecentlyUsedContainer(maxsize=2))
        def add(self, a, b):
            print("Calling add with %r and %r" % (a, b))
            return a + b

    foo = Foo()
    foo.add(1, 1)


def test_standard_functools_deprecated():
    message = "this function will be deprecated in the near future"

    @deprecated(message)
    def foo(n):
        return n + n

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        foo(4)
        assert len(w) == 1
        assert issubclass(w[-1].category, PendingDeprecationWarning)
        assert message == str(w[-1].message)
        assert foo.__name__ == "foo"
