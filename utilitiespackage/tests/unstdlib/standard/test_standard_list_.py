from utilitiespackage.unstdlib.standard.list_ import groupby_count, is_iterable, iterate, iterate_items, iterate_chunks, iterate_flatten, listify


def test_standard_list_groupby_count():
    assert list(groupby_count([1, 1, 1, 2, 3])) == [(1, 3), (2, 1), (3, 1)]
    assert list(groupby_count([0, 0, 0, 1, 1, 2])) == [(0, 3), (1, 2), (2, 1)]


def test_standard_list_is_iterable():
    assert is_iterable("foo") == False
    assert is_iterable(["foo"]) == True
    assert is_iterable(["foo"], unless=list) == False
    assert is_iterable(range(5)) == True


def test_standard_list_iterate():
    assert iterate("foo") == ["foo"]
    assert iterate(["foo"]) == ["foo"]
    assert iterate(["foo"], unless=list) == [["foo"]]
    assert list(iterate(range(5))) == [0, 1, 2, 3, 4]


def test_standard_list_iterate_items():
    assert list(iterate_items({"a": 1})) == [("a", 1)]
    assert list(iterate_items([("a", 1), ("b", 2)])) == [("a", 1), ("b", 2)]


def test_standard_list_iterate_chunks():
    assert list(iterate_chunks([1, 2, 3, 4], size=2)) == [[1, 2], [3, 4]]
    assert list(iterate_chunks([1, 2, 3, 4, 5, 6], size=3)) == [[1, 2, 3], [4, 5, 6]]


def test_standard_list_iterate_flatten():
    assert iterate_flatten([("foo",), ("bar",)]) == ["foo", "bar"]
    assert iterate_flatten([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]


def test_standard_list_listify():
    @listify
    def get_lengths(iterable):
        for i in iterable:
            yield len(i)

    assert get_lengths(["spam", "eggs"]) == [4, 4]

    @listify(wrapper=tuple)
    def get_lengths_tuple(iterable):
        for i in iterable:
            yield len(i)

    assert get_lengths_tuple(["foo", "bar"]) == (3, 3)
