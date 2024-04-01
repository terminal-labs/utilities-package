import os

from pytest_httpserver import HTTPServer

from utilitiespackage.api import api_is_up

PORT_KEY = "PYTEST_HTTPSERVER_PORT"
HOST_KEY = "PYTEST_HTTPSERVER_HOST"
os.environ[HOST_KEY] = "127.0.0.1"
os.environ[PORT_KEY] = "5000"


def test_api_is_up_trycatch():
    assert api_is_up() == False


def test_api_is_up_good(httpserver: HTTPServer):
    assert httpserver.is_running()
    httpserver.expect_request("/api/v1.0/system/test").respond_with_json({"status": "good"})
    assert api_is_up() == True


def test_api_is_up_bad(httpserver: HTTPServer):
    assert httpserver.is_running()
    httpserver.expect_request("/api/v1.0/system/test").respond_with_json({"status": "bad"})
    assert api_is_up() == False
    httpserver.stop()
