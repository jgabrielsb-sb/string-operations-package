# Functions

This section documents the available functions in the `string_operations_package`.

## BASE FUNCTIONS

---

## `get_str_without_accents(text: str) -> str`

Removes all accents from the input string using Unicode normalization.

### ✅ Parameters
- `text` (`str`): The input string from which you want to remove accent marks.

### 🔁 Returns
- `str`: A new string with all accents removed.

### ❌ Raises
- `TypeError`: If the input is not a string.

### 🧪 Example

```
from string_operations_package.base_functions import remove_all_accents

print(remove_all_accents("João"))  # Output: 'Joao'
print(remove_all_accents("Café"))  # Output: 'Cafe'
print(remove_all_accents("String without accents"))  # Output: 'String without accents'
print(remove_all_accents(1)) # raise TypeError
```

## `get_str_without_spaces(text: str) -> str`

Removes all spaces from the input string.

### ✅ Parameters
- `text` (`str`): The input string from which you want to remove spaces.

### 🔁 Returns
- `str`: A new string with all spaces removed.

### ❌ Raises
- `TypeError`: If the input is not a string.

### 🧪 Example

```
from string_operations_package.base_functions import get_str_without_spaces

print(get_str_without_spaces("String with spaces"))  # Output: Stringwithspaces 
print(get_str_without_spaces("StringWithoutSpaces"))  # Output: 'StringWithoutSaces'
print(get_str_without_spaces(1)) # raise TypeError
```

## `get_str_with_only_numbers(text: str) -> str`

Extracts and returns only the numeric characters from the input string.

### ✅ Parameters
- `text` (`str`): The input string from which you want to extract numbers.

### 🔁 Returns
- `str`: A string containing only the numeric characters from the input.

### ❌ Raises
- `TypeError`: If the input is not a string.

### 🧪 Example

```
from string_operations_package.base_functions import get_str_with_only_numbers

print(get_str_with_only_numbers("abc123def456"))  # Output: '123456'
print(get_str_with_only_numbers("no numbers"))    # Output: ''
print(get_str_with_only_numbers(123))              # raise TypeError
```

## `get_formatted_cpf(cpf: str) -> str`

Formats a string of 11 digits into the Brazilian CPF format: XXX.XXX.XXX-XX.

### ✅ Parameters
- `cpf` (`str`): The input string to format (must be exactly 11 digits).

### 🔁 Returns
- `str`: The formatted CPF string.

### ❌ Raises
- `TypeError`: If the input is not a string.
- `ValueError`: If the input string is not 11 digits long or contains non-digit characters.

### 🧪 Example

```
from string_operations_package.business_functions import get_formatted_cpf

print(get_formatted_cpf("12345678901"))    # Output: '123.456.789-01'
print(get_formatted_cpf("1234567890a"))    # raise ValueError
print(get_formatted_cpf("1234567890"))     # raise ValueError
print(get_formatted_cpf(12345678901))       # raise TypeError
```

## BUSSINESS FUNCTIONS 