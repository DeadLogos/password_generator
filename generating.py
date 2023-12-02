import string
import random

Password = str


class EmptyGeneratingRangeError(Exception):
    """
    Unable to generate password due to the lack of selected characters
    """
    pass


def generate_password(length: int, digits: bool, letters: bool, marks: bool) -> Password:
    chars = ''
    if digits:
        chars += string.digits
    if letters:
        chars += string.ascii_letters
    if marks:
        chars += string.punctuation
    if not chars:
        raise EmptyGeneratingRangeError
    return ''.join(random.choice(chars) for _ in range(length))


def generate_multiple_passwords(n: int, length: int, digits: bool, letters: bool, marks: bool) -> list[Password]:
    return [generate_password(length, digits, letters, marks) for _ in range(n)]


def main():
    pass


if __name__ == '__main__':
    main()
