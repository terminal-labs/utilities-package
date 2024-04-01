import threading

import pytest

from utilitiespackage.mock.tcp_server import TCPServer
from utilitiespackage.services import service_is_up


@pytest.fixture(autouse=True)
def mock_tcp_server():
    tcp_server = TCPServer()
    with tcp_server as example_server:
        thread = threading.Thread(target=example_server.listen_for_traffic)
        thread.daemon = True
        thread.start()
        yield example_server


def test_service_is_up():
    assert service_is_up(9500)
