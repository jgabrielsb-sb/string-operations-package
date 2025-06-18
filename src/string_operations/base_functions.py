import unicodedata


def get_str_without_accents(text: str) -> str:
    """
    Remove all accents of a string.
    Args:
        text (str): The input string to remove accents from.
    Returns:
        str: The input string without accents.
    Raises:
        TypeError: If the input is not a string.
    Example:
        >>> get_str_without_accents("João")
        "Joao"
        >>> get_str_without_accents("String without accents")
        "String without accents"
        >>> get_str_without_accents(1)
        TypeError: Input must be a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    str_without_accents = ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
    return str_without_accents

def get_str_without_spaces(text: str) -> str:
    """
    Remove all spaces from a string.
    Args:
        text (str): The input string to remove spaces from.
    Returns:
        str: The input string without spaces.   
    Raises:
        TypeError: If the input is not a string.  
    Example:
        >>> get_str_without_spaces("String with spaces")
        "Stringwithspaces"
        >>> get_str_without_spaces("StringWithoutSpaces")
        "StringWithoutSpaces"
        >>> get_str_without_spaces(1)
        TypeError: Input must be a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    str_without_spaces = text.replace(' ', '')
    return str_without_spaces

def get_str_with_only_numbers(text: str) -> str:
    """
    Get a string with only numbers.
    Args:
        text (str): The input string to get only numbers from.
    Returns:
        str: The input string with only numbers.
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    str_with_only_numbers = ''.join(char for char in text if char.isdigit())
    return str_with_only_numbers