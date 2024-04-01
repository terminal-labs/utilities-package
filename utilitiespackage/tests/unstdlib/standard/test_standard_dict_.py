from utilitiespackage.unstdlib.standard.dict_ import get_many, pop_many


def test_standard_dict_get_many():
    uid, action, limit, offset = get_many({"uid": "123", "action": "abc"}, required=["uid", "action"], optional=["limit", "offset"])
    assert uid == "123"
    assert action == "abc"
    assert limit == None
    assert offset == None
    uid = get_many({"uid": "123", "action": "abc"}, one_of=["uid"])
    assert uid == ["123"]


def test_standard_dict_pop_many():
    items = pop_many({"uid": "123", "action": "abc"}, ["uid", "action"])
    assert items == ["123", "abc"]
