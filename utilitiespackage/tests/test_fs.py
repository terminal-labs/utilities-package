from utilitiespackage.fs import dir_exists, dir_create, dir_delete, file_rename, get_user_home


def test_dir_exists():
    assert dir_exists("/tmp") == True


def test_dir_create():
    assert dir_create("/tmp/testing") == None
    assert dir_create("/tmp/testing/pytest_dir_create") == None


def test_dir_delete():
    assert dir_delete("/tmp/testing/pytest_dir_create") == None


def test_file_rename():
    dir_create("/tmp/testing/pytest_dir_a")
    assert file_rename("/tmp/testing/pytest_dir_a", "/tmp/testing/pytest_dir_b") == None


def test_get_user_home():
    home = get_user_home()
    assert isinstance(home, str)
