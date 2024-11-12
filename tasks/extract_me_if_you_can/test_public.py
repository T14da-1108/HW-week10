from tools.testlib import testlib

from .extract_me_if_you_can import extract_emails, has_vowel, parse_number


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(extract_emails)
    assert testlib.is_function_docstring_exists(has_vowel)
    assert testlib.is_function_docstring_exists(parse_number)


###################
# Tests
###################

def test_extract_emails() -> None:
    assert extract_emails(
        "Hello mister_egor228@gmail.com, I am a Nigerian prince and I want to offer you a business opportunity. Please send me your bank account number to authentic_nigerian_prince@zoo.poo") == [
               'mister_egor228@gmail.com', 'authentic_nigerian_prince@zoo.poo']


def test_extract_emails_single() -> None:
    assert extract_emails("Contact me at john_doe@gmail.com") == ['john_doe@gmail.com']


def test_extract_emails_multiple() -> None:
    assert extract_emails("Emails: first_email123@domain.com, second_email@sub.domain.co") == [
        'first_email123@domain.com', 'second_email@sub.domain.co']


def test_extract_emails_with_no_emails() -> None:
    assert extract_emails("There are no emails here.") == []


def test_extract_emails_with_invalid_format() -> None:
    assert extract_emails("This is not an email: john_doe(at)gmail(dot)com") == []


def test_extract_emails_mixed_content() -> None:
    assert extract_emails(
        "Random text john_doe@gmail.com more random text second_email@domain.com and final text.") == [
               'john_doe@gmail.com', 'second_email@domain.com']


def test_extract_emails_with_underscores_and_digits() -> None:
    assert extract_emails("Emails like user_1234_test@domain.net and admin@site.org are common") == [
        'user_1234_test@domain.net', 'admin@site.org']


def test_has_vowel_true() -> None:
    assert has_vowel("Hello") is True


def test_has_vowel_with_mixed_case() -> None:
    assert has_vowel("HELLO") is True


def test_has_vowel_empty_string() -> None:
    assert has_vowel("") is False


def test_has_vowel_no_vowels() -> None:
    assert has_vowel("brrr") is False


def test_has_vowel_with_special_characters() -> None:
    assert has_vowel("!@#$%^") is False


def test_has_vowel_only_vowels() -> None:
    assert has_vowel("aeiou") is True


def test_has_vowel_with_numbers() -> None:
    assert has_vowel("12345a") is True


def test_parse_number_valid() -> None:
    assert parse_number("My phone number is 123-456-7890.") == ('123', '456', '7890')


def test_parse_number_invalid() -> None:
    assert parse_number("My phone number is 123-456-789.") is None


def test_parse_number_with_text() -> None:
    assert parse_number("My phone number is 321-654-0987.") == ('321', '654', '0987')


def test_parse_number_no_match() -> None:
    assert parse_number("No phone number here.") is None


def test_parse_number_invalid_format() -> None:
    assert parse_number("Invalid phone number 123-45-7890") is None


def test_parse_number_multiple_matches() -> None:
    assert parse_number("Here are two numbers: 123-456-7890 and 321-654-0987.") == ('123', '456', '7890')


def test_parse_number_with_other_characters() -> None:
    assert parse_number("Call me at (123)-456-7890.") is None  # This format is invalid for the function


def test_parse_number_exact_match() -> None:
    assert parse_number("123-456-7890") == ('123', '456', '7890')
