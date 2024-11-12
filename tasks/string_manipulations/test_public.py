import pytest

from tools.testlib import testlib
from .string_manipulations import common_prefix, cut_suffix, boxed, find_all, capwords


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(common_prefix)
    assert testlib.is_function_docstring_exists(cut_suffix)
    assert testlib.is_function_docstring_exists(boxed)
    assert testlib.is_function_docstring_exists(find_all)
    assert testlib.is_function_docstring_exists(capwords)


###################
# Tests
###################

def test_capwords_basic() -> None:
    assert capwords("foo bar baz") == "Foo Bar Baz"


def test_capwords_with_separator() -> None:
    assert capwords("foo,bar boo,", sep=",") == "Foo,Bar boo,"


def test_capwords_empty_separator() -> None:
    with pytest.raises(ValueError):
        capwords("foo,bar", sep="")


def test_capwords_with_extra_spaces() -> None:
    assert capwords(" foo  bar  ") == "Foo Bar"


def test_capwords_newline_characters() -> None:
    assert capwords("foo\nbar\nbaz") == "Foo Bar Baz"


def test_capwords_with_none_separator() -> None:
    assert capwords("hello-world") == "Hello-world"


def test_cut_suffix_basic() -> None:
    assert cut_suffix("foobar", "bar") == "foo"


def test_cut_suffix_no_suffix() -> None:
    assert cut_suffix("foobar", "boo") == "foobar"


def test_cut_suffix_partial_suffix() -> None:
    assert cut_suffix("foobarbar", "bar") == "foobar"


def test_cut_suffix_empty_suffix() -> None:
    assert cut_suffix("foobar", "") == "foobar"


def test_cut_suffix_same_as_string() -> None:
    assert cut_suffix("foobar", "foobar") == ""


def test_cut_suffix_no_suffix_empty_string() -> None:
    assert cut_suffix("", "bar") == ""


def test_boxed_basic() -> None:
    result = boxed("Hello world", fill="*", pad=2)
    expected = (
        "*****************\n"
        "** Hello world **\n"
        "*****************"
    )
    assert result == expected


def test_boxed_single_pad() -> None:
    result = boxed("Fishy", fill="#", pad=1)
    expected = (
        "#########\n"
        "# Fishy #\n"
        "#########"
    )
    assert result == expected


def test_boxed_no_padding() -> None:
    result = boxed("Hi", fill="*", pad=0)
    expected = (
        "**\n"
        "Hi\n"
        "**"
    )
    assert result == expected


def test_boxed_empty_string() -> None:
    result = boxed("", fill="*", pad=2)
    expected = (
        "******\n"
        "**  **\n"
        "******"
    )
    assert result == expected


def test_boxed_zero_pad() -> None:
    result = boxed("Test", fill="-", pad=0)
    expected = (
        "----\n"
        "Test\n"
        "----"
    )
    assert result == expected


def test_boxed_special_fill_char() -> None:
    result = boxed("Special", fill="@", pad=1)
    expected = (
        "@@@@@@@@@@@\n"
        "@ Special @\n"
        "@@@@@@@@@@@"
    )
    assert result == expected


def test_find_all_basic() -> None:
    assert find_all("abracadabra", "a") == [0, 3, 5, 7, 10]


def test_find_all_substring() -> None:
    assert find_all("arara", "ara") == [0, 2]


def test_find_all_no_occurrences() -> None:
    assert find_all("hello world", "x") == []


def test_find_all_overlapping_substring() -> None:
    assert find_all("aaa", "aa") == [0, 1]


def test_find_all_whole_string_as_substring() -> None:
    assert find_all("hello", "hello") == [0]


def test_find_all_single_character() -> None:
    assert find_all("abracadabra", "b") == [1, 8]


def test_common_prefix_basic() -> None:
    assert common_prefix("abra", "abracadabra", "abrasive") == "abra"


def test_common_prefix_no_common_prefix() -> None:
    assert common_prefix("abra", "foobar") == ""


def test_common_prefix_single_string() -> None:
    assert common_prefix("single") == "single"


def test_common_prefix_empty_strings() -> None:
    assert common_prefix("", "", "") == ""


def test_common_prefix_partial_match() -> None:
    assert common_prefix("abc", "abcd", "abxyz") == "ab"


def test_common_prefix_empty_result() -> None:
    assert common_prefix("abc", "def") == ""


def test_common_prefix_all_same() -> None:
    assert common_prefix("same", "same", "same") == "same"
