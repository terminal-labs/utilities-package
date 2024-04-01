from utilitiespackage.unstdlib.standard.type_ import is_subclass


def test_is_subclass():
    assert is_subclass(IOError, Exception) == True
    assert is_subclass(Exception, None) == False
    assert is_subclass(None, Exception) == False
    assert is_subclass(IOError, (None, Exception)) == True
    assert is_subclass(Exception, (None, 42)) == False
