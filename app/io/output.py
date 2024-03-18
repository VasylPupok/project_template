
def write_text(text: str) -> None:
    """
    This function writes text into stdout
    Args:
        text: string, which will be printed into console
    Returns:
        None
    """
    print(str)


def write_file(path: str, text: str) -> bool:
    """
    This function writes text into given file
    Args:
        path: path to given file
        text: string, which will be printed into console
    Returns:
        True when file exists and text was written successfully, otherwise False
    """
    try:
        file = open(path, "a")
        file.write(text)
        return True
    except OSError:
        return False


def overwrite_file(path: str, text: str) -> bool:
    """
    This function writes text into given file using Pandas
    Args:
        path: path to given file
        text: string, which will be printed into console
    Returns:
        True when file exists and text was written successfully, otherwise False
    """
    try:
        file = open(path, "x")
        file.write(text)
        return True
    except OSError:
        return False
