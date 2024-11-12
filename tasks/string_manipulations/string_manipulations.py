from typing import Optional


def capwords(s: str, sep: Optional[str] = None) -> str:  # type: ignore[empty-body]
    """
    Capitalizes the first letter of each word in the given string, using the specified separator.

    :param s: The string to be capitalized.
    :param sep: The separator to use for splitting the string into words.
    :return: A new string where each word starts with a capital letter.
    :raises ValueError: If the separator is an empty string.
    """
    pass


def cut_suffix(s: str, suffix: str) -> str:  # type: ignore[empty-body]
    """
    Removes the specified suffix from the string, if present.

    :param s: The original string.
    :param suffix: The suffix to be removed.
    :return: The string without the specified suffix, or the original string if the suffix is not found.
    """
    pass


def boxed(text: str, fill: str, pad: int) -> str:  # type: ignore[empty-body]
    """
    Returns the string inside a box made of the fill character, with padding around the string.

    :param text: The string to be boxed.
    :param fill: The character used to create the box.
    :param pad: A non-negative integer indicating the amount of padding around the string.
    :return: The string surrounded by a box made of the fill characters.
    """
    pass


def find_all(s: str, sub: str) -> list[int]:  # type: ignore[empty-body]
    """
    Finds all occurrences of a substring in a given string and returns their starting indices.

    :param s: The string to search within.
    :param sub: The substring to find.
    :return: A list of indices where the substring occurs in the string.
    """
    pass


def common_prefix(*strings: str) -> str:  # type: ignore[empty-body]
    """
    Finds the longest common prefix among a set of strings.

    :param strings: One or more strings to compare.
    :return: The longest common prefix among the given strings, or an empty string if none exists.
    """
    pass
