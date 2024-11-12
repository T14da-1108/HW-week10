# You might want to use this library.
# import re

def extract_emails(text: str) -> list[str]:  # type: ignore[empty-body]
    """
    Extracts all valid email addresses from the given text.

    :param text: The string to extract email addresses from.
    :return: A list of email addresses found in the text.
    """
    pass


def has_vowel(text: str) -> bool:  # type: ignore[empty-body]
    """
    Returns True if the string contains any vowels (a, e, i, o, u), otherwise False.

    :param text: The string to check for vowels.
    :return: True if the string contains at least one vowel, False otherwise.
    """
    pass


def parse_number(text: str) -> tuple[str, ...]:  # type: ignore[empty-body]
    """
    Parses a phone number in the format {area code}-{local exchange}-{line number} from the text.

    :param text: The string containing the phone number.
    :return: A tuple with (area code, local exchange, line number) if found, otherwise None.
    """
    pass
