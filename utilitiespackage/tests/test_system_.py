from utilitiespackage.system import abort, set_env_var, get_env_var


def test_abort():
    abort("done", fake=True) == {"faked": True, "exitcode": 0}


def test_set_env_var():
    assert set_env_var("var0", "some data", "test") == None
    assert get_env_var("var0", "test") == "some data"


def test_get_env_var():
    assert set_env_var("var1", "some data", "test") == None
    assert get_env_var("var1", "test") == "some data"
