from generating import Password
import config
from typing import Iterable
from generating import generate_multiple_passwords


class DumpDataError(Exception):
    """
    Unable to save data in file
    """


def dump_passwords(passwords: Iterable[Password]) -> None:
    """
    Save list of passwords into txt file, line by line
    :param passwords: list[Passwords]
    """
    try:
        with open(config.DUMP_FILENAME, 'w', encoding='utf-8') as file:
            print(*passwords, sep='\n', end='', file=file)
    except Exception:
        raise DumpDataError


def main():
    pass


if __name__ == '__main__':
    main()
