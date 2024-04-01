import os
import json

import pytest

from utilitiespackage.configs import get_json_dict_from_dir


@pytest.fixture
def tmpfiles():
    if not os.path.exists("/tmp/testing"):
        os.mkdir("/tmp/testing")
    if not os.path.exists("/tmp/testing/mockfiles"):
        os.mkdir("/tmp/testing/mockfiles")
    if not os.path.exists("/tmp/testing/mockfiles/jsondir"):
        os.mkdir("/tmp/testing/mockfiles/jsondir")

    if not os.path.exists("/tmp/testing/mockfiles/jsondir/a.json"):
        with open("/tmp/testing/mockfiles/jsondir/a.json", "w") as file:
            dict = {"name": "messenger", "metadata": "more info for a"}
            json_dict = json.dumps(dict)
            file.write(json_dict)

    if not os.path.exists("/tmp/testing/mockfiles/jsondir/b.json"):
        with open("/tmp/testing/mockfiles/jsondir/b.json", "w") as file:
            dict = {"name": "messenger", "metadata": "more info for b"}
            json_dict = json.dumps(dict)
            file.write(json_dict)


def test_get_json_dict_from_dir(tmpfiles):
    dict = get_json_dict_from_dir("a", "/tmp/testing/mockfiles/jsondir")
    assert dict == {"metadata": "more info for a", "name": "messenger"}
    dict = get_json_dict_from_dir("b", "/tmp/testing/mockfiles/jsondir")
    assert dict == {"metadata": "more info for b", "name": "messenger"}
