import operator
from functools import partial

from utilitiespackage.yunobuiltin import (
    get,
    gensym,
    isa,
    interleave,
    is_even,
    is_iterable,
    new_list,
    new_iter,
    new_tuple,
    juxt,
    flatten,
    is_str_or_bytes,
    identity,
    is_map,
    is_seq,
    append,
    prepend,
    MultiFn,
    pipeline,
    rpartial,
    juxt,
    thread,
    concat,
    assoc,
    assoc_deep,
    assoc_kw,
    assoc_deep_kw,
    interleave,
    assoc_in,
    assoc_deep_in,
    update_in,
    update_deep_in,
    dissoc,
    dissoc_deep,
    dissoc_in,
    dissoc_deep_in,
    select_keys,
    select_vals,
    if_let,
    get_in,
    better_map,
)


def test_better_map():
    def addition(*args):
        return args

    numbers = ([2, 4, 6, 8], [2, 4, 6, 8])
    result = list(better_map(addition, numbers, numbers))
    assert result == [([2, 4, 6, 8], [2, 4, 6, 8]), ([2, 4, 6, 8], [2, 4, 6, 8])]
    numbers = ([2, 4, 6, 8], [2, 4, 6, 8])
    result = list(better_map(addition, numbers))
    assert result == [(2, 4, 6, 8), (2, 4, 6, 8)]


def test_get_in():
    d_0 = {"a": 0, "b": 0}
    assert get_in(d_0, "a") == 0


def test_if_let():
    def run_if_true(expression):
        return True

    def run_if_false(expression):
        return False

    assert if_let(0 < 1, run_if_true, run_if_false) == True
    assert if_let(1 < 0, run_if_true, run_if_false) == False
    assert if_let(0 < 1, True, False) == True
    assert if_let(1 < 0, True, False) == False


def test_select_vals():
    d_0 = {"a": 0, "b": 0}
    assert select_vals(("a"), d_0) == [0]
    d_0 = {"a": 0, "b": 1, "c": 2}
    assert select_vals(("a", "b"), d_0) == [0, 1]


def test_select_keys():
    d_0 = {"a": 0, "b": 0}
    assert select_keys(("a"), d_0) == {"a": 0}
    d_0 = {"a": 0, "b": 0, "c": 0}
    assert select_keys(("a", "b"), d_0) == {"a": 0, "b": 0}


def test_dissoc_deep_in():
    d_0 = {"a": 0}
    assert dissoc_deep_in(d_0, ("a")) == {}
    d_0 = {"a": None}
    assert dissoc_deep_in(d_0, ("a", "b")) == {"a": None}
    d_0 = {"a": {"b": 0}}
    assert dissoc_deep_in(d_0, ("a", "b")) == {"a": {}}


def test_dissoc_in():
    d_0 = {"a": 0}
    assert dissoc_in(d_0, ("a")) == {}
    d_0 = {"a": None}
    assert dissoc_in(d_0, ("a", "b")) == {"a": None}
    d_0 = {"a": {"b": 0}}
    assert dissoc_in(d_0, ("a", "b")) == {"a": {}}


def test_dissoc_deep():
    d_0 = {"a": 0}
    assert dissoc_deep(d_0, "a") == {}


def test_dissoc():
    d_0 = {"a": 0}
    assert dissoc(d_0, "a") == {}


def test_update_deep_in():
    def fn(current_value, *args, **kwargs):
        return "new data"

    d_0 = {"a": 0}
    assert update_deep_in(d_0, ["a"], fn) == {"a": "new data"}

    def fn(current_value, args, debug=False):
        if len(args) > 0:
            if args[0] == "add 10":
                return "new data + 10"

    d_0 = {"a": 0}
    assert update_deep_in(d_0, ["a"], fn, ["add 10"], debug=True) == {"a": "new data + 10"}
    d_0 = {"a": {}}
    assert update_deep_in(d_0, ["a", "b"], fn, ["add 10"], debug=True) == {"a": {"b": "new data + 10"}}


def test_update_in():
    def fn(current_value, *args, **kwargs):
        return "new data"

    d_0 = {"a": 0}
    assert update_in(d_0, ["a"], fn) == {"a": "new data"}

    def fn(current_value, args, debug=False):
        if len(args) > 0:
            if args[0] == "add 10":
                return "new data + 10"

    d_0 = {"a": 0}
    assert update_in(d_0, ["a"], fn, ["add 10"], debug=True) == {"a": "new data + 10"}
    d_0 = {"a": {}}
    assert update_in(d_0, ["a", "b"], fn, ["add 10"], debug=True) == {"a": {"b": "new data + 10"}}


def test_assoc_deep_in():
    d_0 = {"c": 3}
    d_1 = {"d": 3}
    assert assoc_deep_in(d_0, ["a", "b"], ["a", "b"]) == {"a": {"b": ["a", "b"]}, "c": 3}
    assert assoc_deep_in(d_1, ["a", "b", "c"], ["a", "b"]) == {"a": {"b": {"c": ["a", "b"]}}, "d": 3}


def test_assoc_in():
    d_0 = {"c": 3}
    d_1 = {"d": 3}
    assert assoc_in(d_0, ["a", "b"], ["a", "b"]) == {"a": {"b": ["a", "b"]}, "c": 3}
    assert assoc_in(d_1, ["a", "b", "c"], ["a", "b"]) == {"a": {"b": {"c": ["a", "b"]}}, "d": 3}


def test_interleave():
    a = [0, 2, 4, 6]
    b = [1, 3, 5, 7]
    assert list(interleave(a, b)) == [0, 1, 2, 3, 4, 5, 6, 7]


def test_assoc_kw():
    d_0 = {"a": 0, "b": 1}
    assert assoc_kw(d_0, a=1, b=2) == {"a": 1, "b": 2}
    d_0 = None
    assert assoc_kw(d_0, a=0, b=1) == {"a": 0, "b": 1}


def test_assoc_deep_kw():
    d_0 = {"a": 0, "b": 1}
    assert assoc_deep_kw(d_0, a=1, b=2) == {"a": 1, "b": 2}
    d_0 = None
    assert assoc_deep_kw(d_0, a=0, b=1) == {"a": 0, "b": 1}


def test_assoc():
    d_0 = {"a": 0, "b": 1}
    assert assoc(d_0, "a", 7, "b", 8) == {"a": 7, "b": 8}
    d_0 = None
    assert assoc(d_0, "a", 7, "b", 8) == {"a": 7, "b": 8}


def test_assoc_deep():
    d_0 = {"a": 0, "b": 1}
    assert assoc_deep(d_0, "a", 7, "b", 8) == {"a": 7, "b": 8}
    d_0 = None
    assert assoc_deep(d_0, "a", 7, "b", 8) == {"a": 7, "b": 8}


def test_concat():
    a = [0, 1, 2, 3]
    b = [4, 5, 6, 7]
    assert list(concat(a, b)) == [0, 1, 2, 3, 4, 5, 6, 7]
    i_a = 0
    i_b = 1
    assert list(concat(i_a, i_b)) == [0, 1]
    d_a = {"a": 0}
    d_b = {"b": 1}
    assert list(concat(d_a, d_b)) == ["a", "b"]


def test_gensym():
    identifier = gensym()
    assert isinstance(identifier, str)


def test_isa():
    assert isa(1, 1)

    class NewStyleClass(object):
        pass

    nsc = NewStyleClass()
    assert isa(nsc, object)


def test_is_even():
    assert is_even(2)


def test_is_iterable():
    assert is_iterable([])


def test_new_list():
    assert new_list(1, 2, 3) == [1, 2, 3]


def test_new_iter():
    assert list(new_iter(1, 2, 3)) == [1, 2, 3]


def test_new_tuple():
    assert new_tuple(1, 2, 3) == (1, 2, 3)


def test_flatten():
    assert list(flatten([[[1, 2, 3]]])) == [1, 2, 3]


def test_is_str_or_bytes():
    assert is_str_or_bytes("test")
    assert is_str_or_bytes(123) == False


def test_identity():
    assert identity(1) == 1


def test_is_map():
    assert is_map({"abc": 123})


def test_is_seq():
    assert is_seq([1, 2, 3])


def test_append():
    assert append([], 1, 2, 3) == [1, 2, 3]
    assert list(append([0], 1, 2, 3)) == [0, 1, 2, 3]
    assert append([], 1, 2, 3) == [1, 2, 3]
    assert list(append([0], 1, 2, 3)) == [0, 1, 2, 3]


def test_prepend():
    assert list(prepend([-1, 0], [1, 2, 3])) == [-1, 0, 1, 2, 3]
    assert list(prepend(1, [1, 2, 3])) == [1, 1, 2, 3]


def test_MultiFn():
    def test_func1():
        pass

    def test_func2(*args, **kwargs):
        pass

    mfunc = MultiFn(test_func1)
    mfunc.default_func = test_func2
    mfunc.invoke("mfunc", {"test": "abc"}, {"test": "abc"})
    mfunc.register_default(test_func2)
    mfunc.unregister_default()
    mfunc.__call__()


def test_pipeline():
    five = partial(operator.add, 5)
    ten = partial(operator.add, 10)
    one = partial(operator.add, 1)

    assert pipeline(five, ten, one)(0) == 16


def test_rpartial():
    func = rpartial(get, 0)
    assert func([0]) == 0


def test_juxt():
    def test_func1(a, b, c):
        return "data 1"

    def test_func2(a, b, c):
        return "data 2"

    func = juxt(test_func1, test_func2)
    assert list(func(1, 2, 3)) == ["data 1", "data 2"]


def test_thread():
    assert thread(10, lambda x: x + 1, lambda x: x * 2) == 22
