"""Various tools for the development process."""

# stdlib
from typing import Callable

def function_name(f) -> Callable[..., None]:
    """Prints the function name"""
    def wrapper():
        print("=" * 33)
        print(f.__name__)
        print()
    return wrapper
