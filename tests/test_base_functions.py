from string_operations.base_functions import (
    get_str_without_accents,
    get_str_without_spaces,
    get_str_with_only_numbers
)

import pytest

######## REMOVE_ALL_ACCENTS TESTS ########
def test_string_with_accents():
    """Test if a string with accents is converted to a string without accents."""
    input_str = "João está no café."
    expected = "Joao esta no cafe."
    assert get_str_without_accents(input_str) == expected

def test_string_without_accents():
    """Test if a string without accents remains the same."""
    input_str = "Simple text"
    expected = "Simple text"
    assert get_str_without_accents(input_str) == expected

def test_string_with_numbers():
    """Test if a string with numbers retains the numbers."""
    input_str = "Café 123"
    expected = "Cafe 123"
    assert get_str_without_accents(input_str) == expected

def test_string_with_special_characters():
    """Test if a string with special characters remains the same."""
    input_str = "Olá! Como vai? #python"
    expected = "Ola! Como vai? #python"
    assert get_str_without_accents(input_str) == expected

def test_invalid_input_type_remove_all_accents():
    with pytest.raises(TypeError):
        get_str_without_accents(12345)
        
######## REMOVE_ALL_SPACES TESTS ########
def test_string_with_spaces():
    """Test if a string with spaces is converted to a string without spaces."""
    input_str = "This is a test"
    expected = "Thisisatest"
    assert get_str_without_spaces(input_str) == expected

def test_string_without_spaces():
    """Test if a string without spaces remains the same."""
    input_str = "AlreadyClean"
    expected = "AlreadyClean"
    assert get_str_without_spaces(input_str) == expected

def test_invalid_input_type_remove_all_spaces():
    with pytest.raises(TypeError):
        get_str_without_spaces(12345)
        
######## GET_STR_WITH_ONLY_NUMBERS TESTS ########
def test_string_with_numbers():
    """Test if a string with numbers is converted to a string with only numbers."""
    input_str = "12345"
    expected = "12345"
    assert get_str_with_only_numbers(input_str) == expected
    
def test_string_without_numbers():
    """Test if a string without numbers will return an empty string."""
    input_str = "NoNumbersHere"
    expected = ""
    assert get_str_with_only_numbers(input_str) == expected
    
def test_invalid_input_type_only_numbers():
    with pytest.raises(TypeError):
        get_str_with_only_numbers(12345)
        
