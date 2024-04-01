import sys

del sys.modules["utilitiespackage.derived_settings"]
from utilitiespackage.derived_settings import APPDIR


def test_set_vars():
    assert isinstance(APPDIR, str)
