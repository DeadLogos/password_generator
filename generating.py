import string
import random
from typing import Iterable

Password = str


class EmptyGeneratingRangeError(Exception):
    """
    Unable to generate password due to the lack of selected characters
    """
    pass


def combine_selected_chars(digits: bool, letters: bool, marks: bool) -> str:
    """
    Validate the selection of character categories for password generation and combine them.
    :return: Combined string of selected character categories
    :raises EmptyGeneratingRangeError: If no character category is selected
    """
    chars = ''
    if digits:
        chars += string.digits
    if letters:
        chars += string.ascii_letters
    if marks:
        chars += string.punctuation
    if not chars:
        raise EmptyGeneratingRangeError
    return chars


def generate_password(length: int, chars: str) -> Password:
    """
    Generate a password based on given parameters.
    :param length: Length of the password
    :param chars: Character range
    :return: Generated password as a string
    """
    return ''.join(random.choice(chars) for _ in range(length))


def generate_multiple_passwords(n: int, length: int, digits: bool, letters: bool, marks: bool) -> Iterable[Password]:
    """
    Generate multiple passwords based on given parameters.
    :param n: Number of passwords to generate
    :param length: Length of each password
    :param digits: Whether to include digits in the passwords
    :param letters: Whether to include letters in the passwords
    :param marks: Whether to include special characters in the passwords
    :return: Iterable of generated passwords as strings
    """
    chars = combine_selected_chars(digits, letters, marks)
    return (generate_password(length, chars) for _ in range(n))


def main():
    pass


if __name__ == '__main__':
    main()
