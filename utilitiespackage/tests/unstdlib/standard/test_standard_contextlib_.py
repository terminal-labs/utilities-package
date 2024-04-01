import os

from utilitiespackage.unstdlib.standard.contextlib_ import open_atomic, _doctest_setup


def test_standard_contextlib_open_atomic():
    _doctest_setup()
    f = open_atomic("/tmp/open_atomic-example.txt")
    assert f.temp_name == "/tmp/.open_atomic-example.txt.temp"
    f.write("Hello, world!")
    f.close()
    f.close()
    assert os.path.exists("/tmp/open_atomic-example.txt")
