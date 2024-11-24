def caesar_encrypt(text: str, key: int) -> str:
    """
    Encrypts the string passed to it using the Caesar cipher with a key n.

    :param text: The string to be encrypted.
    :param key: An integer representing the cipher key, which can be positive or negative.
    :return: The encrypted string.
    """
    # Normalize the key to be within the range of 0-25
    key = key % 26

    # Create translation tables for lowercase and uppercase letters
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Create translation for both lowercase and uppercase letters with the given shift key
    translation_table = str.maketrans(
        lower_case + upper_case,
        lower_case[key:] + lower_case[:key] + upper_case[key:] + upper_case[:key]
    )

    # Return the encrypted text using the translation table
    return text.translate(translation_table)
