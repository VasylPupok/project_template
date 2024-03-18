import os

import pandas
from pandas import read_fwf, read_csv


def read_text(prompt: str) -> str:
    """
    This function reads user input from stdin and returns this text as string
    Args:
        prompt: text, printed into stdout before reading user input
    Returns:
        text, printed by user
    """
    return input(prompt)


def read_file(path: str) -> str|None:
    """
    This function reads text from file and returns this text as string
    Args:
        path: path to file, where text will be read
    Returns:
        text in given file, or None in case of error
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except OSError:
        return None


def read_csv_pandas(path: str) -> pandas.DataFrame|None:
    """
    This function reads text from file and returns this text as string
    Uses Pandas library for implementation
    Args:
        path: path to file, where text will be read
    Returns:
        text in given file, or None in case of error
    """
    if os.path.isfile(path):
        return read_csv(path, dtype=str)
    return None
