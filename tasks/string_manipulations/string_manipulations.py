from typing import Optional


def capwords(s: str, sep: Optional[str] = None) -> str:
    """
    Capitalizes the first letter of each word in the given string, using the specified separator.

    :param s: The string to be capitalized.
    :param sep: The separator to use for splitting the string into words.
    :return: A new string where each word starts with a capital letter.
    :raises ValueError: If the separator is an empty string.
    """
    if sep == "":
        raise ValueError("empty separator")

    # If sep is None, use the default behavior (split by any whitespace)
    if sep is None:
        return " ".join([word.capitalize() for word in s.split()])

    # Otherwise, split by the provided separator
    return sep.join([word.capitalize() for word in s.split(sep)])


def cut_suffix(s: str, suffix: str) -> str:
    """
    Removes the specified suffix from the string, if present.

    :param s: The original string.
    :param suffix: The suffix to be removed.
    :return: The string without the specified suffix, or the original string if the suffix is not found.
    """
    if suffix == "":
        return s  # empty suffix, return the original string

    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s


def boxed(text: str, fill: str, pad: int) -> str:
    """
    Returns the string inside a box made of the fill character, with padding around the string.

    :param text: The string to be boxed.
    :param fill: The character used to create the box.
    :param pad: A non-negative integer indicating the amount of padding around the string.
    :return: The string surrounded by a box made of the fill characters.
    """
    if pad < 0:
        raise ValueError("pad must be non-negative")

    if pad == 0:
        border = fill * len(text)
        middle = text
    else:
        border = fill * (len(text) + 2 + 2 * pad)  # Add padding to the borders
        middle = f"{fill * pad} {text} {fill * pad}"  # Add padding around the text

    return f"{border}\n{middle}\n{border}"


def find_all(s: str, sub: str) -> list[int]:
    """
    Finds all occurrences of a substring in a given string and returns their starting indices.

    :param s: The string to search within.
    :param sub: The substring to find.
    :return: A list of indices where the substring occurs in the string.
    """
    return [i for i in range(len(s)) if s.startswith(sub, i)]


def common_prefix(*strings: str) -> str:
    """
    Finds the longest common prefix among a set of strings.

    :param strings: One or more strings to compare.
    :return: The longest common prefix among the given strings, or an empty string if none exists.
    """
    if not strings:
        return ""

    # Find the smallest string length to limit comparisons
    min_length = min(len(s) for s in strings)

    # Compare character by character
    prefix = []
    for i in range(min_length):
        char = strings[0][i]
        if all(s[i] == char for s in strings):
            prefix.append(char)
        else:
            break

    return "".join(prefix)
