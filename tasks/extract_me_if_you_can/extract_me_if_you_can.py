import re


def extract_emails(text: str) -> list[str]:
    """
    Extracts all valid email addresses from the given text.

    :param text: The string to extract email addresses from.
    :return: A list of email addresses found in the text.
    """

    email_pattern = r'[A-Za-z0-9_]+@[A-Za-z0-9_-]+\.[A-Za-z0-9.-]+'
    return re.findall(email_pattern, text)


def has_vowel(text: str) -> bool:
    """
    Returns True if the string contains any vowels (a, e, i, o, u), otherwise False.

    :param text: The string to check for vowels.
    :return: True if the string contains at least one vowel, False otherwise.
    """
    return bool(re.search(r'[aeiouAEIOU]', text))


def parse_number(text: str) -> tuple[str, ...]:
    """
    Parses a phone number in the format {area code}-{local exchange}-{line number} from the text.

    :param text: The string containing the phone number.
    :return: A tuple with (area code, local exchange, line number) if found, otherwise None.
    """
    phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
    match = re.search(phone_pattern, text)
    if match:
        return match.groups()
    return None
