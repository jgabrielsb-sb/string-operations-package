# Functions

This section documents the available functions in the `string_operations_package`.

---

## `remove_all_accents(text: str) -> str`

Removes all accents from the input string using Unicode normalization.

### ✅ Parameters
- `text` (`str`): The input string from which you want to remove accent marks.

### 🔁 Returns
- `str`: A new string with all accents removed.

### ❌ Raises
- `TypeError`: If the input is not a string.

### 🧪 Example

```
from string_operations_package import remove_all_accents

print(remove_all_accents("João"))  # Output: 'Joao'
print(remove_all_accents("Café"))  # Output: 'Cafe'
print(remove_all_accents("String without accents"))  # Output: 'String without accents'
print(remove_all_accents(1)) # raise TypeError
```