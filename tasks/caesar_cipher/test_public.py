from tools.testlib import testlib
from .caesar_cipher import caesar_encrypt


###################
# Structure asserts
###################

def test_is_input_unchanged() -> None:
    input_str = "HELLO"
    key = 5
    is_unchanged = testlib.is_input_unchanged(caesar_encrypt, (input_str, key))
    assert is_unchanged, "Input string was modified"


def test_docs() -> None:
    assert testlib.is_function_docstring_exists(caesar_encrypt)


###################
# Tests
###################


def test_caesar_encrypt_positive_key() -> None:
    assert caesar_encrypt("HELLO", 3) == "KHOOR"


def test_caesar_encrypt_negative_key() -> None:
    assert caesar_encrypt("KHOOR", -3) == "HELLO"


def test_caesar_encrypt_wrap_around_positive() -> None:
    assert caesar_encrypt("XYZ", 3) == "ABC"


def test_caesar_encrypt_wrap_around_negative() -> None:
    assert caesar_encrypt("ABC", -3) == "XYZ"


def test_caesar_encrypt_non_alphabetical() -> None:
    assert caesar_encrypt("HELLO WORLD!", 3) == "KHOOR ZRUOG!"


def test_caesar_encrypt_empty_string() -> None:
    assert caesar_encrypt("", 3) == ""


def test_caesar_encrypt_mixed_case() -> None:
    assert caesar_encrypt("Hello World", 5) == "Mjqqt Btwqi"


def test_caesar_encrypt_key_zero() -> None:
    assert caesar_encrypt("HELLO", 0) == "HELLO"


def test_caesar_encrypt_large_key() -> None:
    assert caesar_encrypt("HELLO", 29) == "KHOOR"


def test_caesar_encrypt_large_negative_key() -> None:
    assert caesar_encrypt("HELLO", -29) == "EBIIL"
