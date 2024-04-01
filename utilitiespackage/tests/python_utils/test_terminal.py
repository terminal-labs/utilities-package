from utilitiespackage.python_utils.terminal import get_terminal_size


def test_get_terminal_size():
    results = get_terminal_size()
    assert len(results) == 2
    assert isinstance(results, tuple) == True
