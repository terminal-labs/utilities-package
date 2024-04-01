import sys

del sys.modules["utilitiespackage.settings"]
from utilitiespackage.settings import (
    VERSION,
    PRINT_VERBOSITY,
    EXCLUDED_DIRS,
    PROJECT_NAME,
    TEMPDIR,
    TEXTTABLE_STYLE,
    DIRS,
    MINIMUM_PYTHON_VERSION,
    COVERAGERC_PATH,
)


def test_settings_version():
    assert type(VERSION) == str


def test_settings_print_verbosity():
    assert PRINT_VERBOSITY == "high" or PRINT_VERBOSITY == "low"


def test_settings_excluded_dirs():
    assert isinstance(EXCLUDED_DIRS, list)


def test_settings_project_name():
    assert isinstance(PROJECT_NAME, str)


def test_settings_project_name():
    assert isinstance(PROJECT_NAME, str)


def test_settings_tempdir():
    assert isinstance(TEMPDIR, str)


def test_settings_textable_style():
    assert isinstance(TEXTTABLE_STYLE, list)


def test_settings_dirs():
    assert isinstance(DIRS, list)


def test_settings_minimum_python_version():
    assert isinstance(MINIMUM_PYTHON_VERSION, tuple)


def test_settings_coveragerc_path():
    assert isinstance(COVERAGERC_PATH, str)
