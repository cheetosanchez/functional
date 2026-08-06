from functools import reduce
from typing import Callable

# Complete the apply_transform function. It should accept:

# A list of strings
# A transformation function that accepts one string and returns one string
# Apply the transformation to every string and return the results in a new list. Preserve the original order.

# Add accurate type hints to both parameters and the return value. Use Callable[[str], str] for the transformation function.
# must not import any modules other than Callable.
# must not use reduce, map, or filter.


def apply_transform(strings: list[str], transform: Callable[[str], str]) -> list[str]:
    if not strings:
        return []
    transformed_strings = []
    for string in strings:
        transformed_strings.append(transform(string))
    return transformed_strings
