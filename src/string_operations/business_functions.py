
def get_formatted_cpf(cpf: str) -> str:
    """
    Format the string to the Brazilian CPF format: XXX.XXX.XXX-XX
    Args:
        cpf (str): The input string to format.
    Returns:
        str: The input string formatted to the Brazilian CPF format.
    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is not 11 digits long or contains non-digit characters.
    Example:
        >>> get_formatted_cpf("12345678901")
        "123.456.789-01"
        >>> get_formatted_cpf("1234567890212")
        ValueError: CPF must be a string of exactly 11 digits.
        >>> get_formatted_cpf(12345678901)
        TypeError: Input must be a string
    """
    
    if not isinstance(cpf, str):
        raise TypeError("Input must be a string")
    
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF must be a string of exactly 11 digits.")
    
    formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return formatted_cpf