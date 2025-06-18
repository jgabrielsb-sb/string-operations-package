from string_operations.business_functions import (
    get_formatted_cpf
)

import pytest

######## GET_FORMATTED_CPF TESTS ########
def test_value_error_when_cpf_is_not_a_string():
    with pytest.raises(TypeError):
        get_formatted_cpf(12345678901)
        
def test_value_error_when_cpf_has_more_than_11_digits():
    with pytest.raises(ValueError):
        get_formatted_cpf('1234567890345312')
    
def test_value_error_when_cpf_has_less_than_11_digits():
    with pytest.raises(ValueError):
        get_formatted_cpf('03453')
        
def test_value_error_when_cpf_has_non_digit_characters():
    with pytest.raises(ValueError):
        get_formatted_cpf('1234567890345312a')
        
def test_correct_cpf_is_formatted():
    assert get_formatted_cpf('03453123456') == '034.531.234-56'
    assert isinstance(get_formatted_cpf('03453123456'), str)