import os
import sys
import click
import pytest

from utilitiespackage.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION


@click.group()
def cli():
    return None


@click.group(name="system")
def system_group():
    return None


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    os.chdir(TESTDIR)
    pytest.main(["--disable-pytest-warnings", "-x", "-v", TESTDIR])


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    os.chdir(APPDIR)
    pytest.main(["--disable-pytest-warnings", f"--cov-config={COVERAGERC_PATH}", "--cov=utilitiespackage", "--cov-report", "term-missing", APPDIR])


cli.add_command(system_group)
main = cli
