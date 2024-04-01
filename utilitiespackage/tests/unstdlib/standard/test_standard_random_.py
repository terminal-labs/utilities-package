import sys

del sys.modules["utilitiespackage.unstdlib.standard"]
from utilitiespackage.unstdlib.standard.random_ import set_random


def test_set_random():
    vars = set_random()
    assert isinstance(vars, dict)
    assert len(vars.keys()) == 1
