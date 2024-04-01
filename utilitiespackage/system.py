import sys
import os

from termcolor import colored


def abort(message, fake=False):
    if not fake:
        sys.exit(colored("".join(["ABORTED - ", message]), "red", attrs=["bold"]))  # pragma: no cover
    else:
        return {"faked": True, "exitcode": 0}


def set_env_var(name, value, prefix):
    """Set an environment variable in all caps that is prefixed
    """
    os.environ[prefix.upper() + "_" + name.upper()] = value


def get_env_var(name, prefix):
    """Get an environment variable in all caps that is prefixed
    """
    return os.environ.get(prefix.upper() + "_" + name.upper())
