import sys
import pytest

from utilitiespackage.crypto import aes_encrypt, aes_decrypt


@pytest.mark.skipif(sys.platform.startswith("darwin") == True, reason="mac has unsupported version of openssl")
def test_aes_encrypt():
    assert aes_decrypt(aes_encrypt("plaintext", "password"), "password") == b"plaintext"


@pytest.mark.skipif(sys.platform.startswith("darwin") == True, reason="mac has unsupported version of openssl")
def test_aes_decrypt():
    assert aes_decrypt(b"U2FsdGVkX1/5WxdnwB9+rUwtU09n4/3Kp3HauNL1z94=", "password") == b"plaintext"
