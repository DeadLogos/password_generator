from generating import Password
import config
from typing import Iterable
from generating import generate_multiple_passwords
from pathlib import Path


class DumpDataError(Exception):
    """
    Unable to save data in file
    """


def dump_passwords(passwords: Iterable[Password], on_desktop=False) -> None:
    """
    Save list of passwords into txt file, line by line
    :param passwords: list[Passwords]
    :param on_desktop: bool
    """
    try:
        path = Path(config.DESKTOP_DIR if on_desktop else '') / config.DUMP_FILENAME
        with open(path, 'w', encoding='utf-8') as file:
            print(*passwords, sep='\n', end='', file=file)
    except Exception:
        raise DumpDataError


def main():
    pass


if __name__ == '__main__':
    main()
