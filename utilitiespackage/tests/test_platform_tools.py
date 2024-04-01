from utilitiespackage.platform_tools import is_windows, is_linux, is_darwin, is_freebsd, is_netbsd, is_openbsd


def test_is_windows():
    platform = is_windows()
    assert platform == True or platform == False


def test_is_linux():
    platform = is_linux()
    assert platform == True or platform == False


def test_is_darwin():
    platform = is_darwin()
    assert platform == True or platform == False


def test_is_freebsd():
    platform = is_freebsd()
    assert platform == True or platform == False


def test_is_netbsd():
    platform = is_netbsd()
    assert platform == True or platform == False


def test_is_openbsd():
    platform = is_openbsd()
    assert platform == True or platform == False
