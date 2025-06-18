
import unicodedata

def remove_all_accents(text: str) -> str:
    """
    Remove all accents of a string.
    
    Args:
        text (str): The input string to remove accents from.
        
    Returns:
        str: The input string without accents.
        
    Raises:
        TypeError: If the input is not a string.
        
    Example:
        >>> remove_all_accents("João")
        "Joao"
        >>> remove_all_accents("String without accents")
        "String without accents"
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')