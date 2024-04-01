from utilitiespackage.python_utils import about_


def test_definitions():
    # The setup.py requires this so we better make sure they exist :)
    assert about_.__version__
    assert about_.__author__
    assert about_.__author_email__
    assert about_.__description__
