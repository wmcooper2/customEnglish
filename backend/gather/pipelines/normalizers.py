"""Text normalization pipeline and functions."""

# std lib
import functools
from string import whitespace, punctuation
from typing import Any, Callable, List, Optional, Text


def compose(*functions: Callable[..., Any]) -> Callable[..., Any]:
    """Compose chain of functions"""

    def _inner_compose(functA, functB) -> Callable[..., Any]:
        """Wraps the second function with the first."""

#             print(functB.__name__)  # functA is lambda, functB is being composed
        return lambda x: functA(functB(x))
    return functools.reduce(_inner_compose, functions, lambda x: x)


def normalize(text: Text, functions: List[Callable[..., Any]]) -> Optional[Callable[..., Any]]:
    """Normalize the base text."""

    if text:
        # methods composed from end to beginning of list
        composition = compose(*functions)
        return composition(text)
    return None


def remove_blank_elements(data: List[Text]) -> List[Text]:
    """Remove empty elements from the list."""

    return [element for element in data if element]


def remove_html_character_entities(data: List[Text]) -> List[Text]:
    """Remove html character entities."""

    return [line.replace('\xa0', ' ') for line in data]


def remove_newline_chars(data: List[Text]) -> List[Text]:
    """Remove all '\\n' from the data."""

    string = str(data)
    string.replace(r"\n", "")
    return string.split()


def remove_punctuation(data: List[Text]) -> List[Text]:
    """Remove all punctuation found in string.punctuation."""

    cleaned = []
    string = str(data)
    for letter in string:
        if letter not in punctuation:
            cleaned.append(letter)
    return ("".join(cleaned)).split(" ")


def remove_whitespace(data: List[Text]) -> List[Text]:
    """Remove any whitespace characters from each line."""

    return [line for line in data if line not in whitespace]


def strip_lines(data: List[Text]) -> List[Text]:
    """Strip the whitespace from the beginning and end of each line."""

    return [line.strip() for line in data]


def tokenize(data: Text) -> List[Text]:
    """Tokenize data into words."""
    return data.split(" ")


if __name__ == "__main__":
    TEXT_LIST = ["This is a multi-line",
            "a newline:\n",
            "example of text with characters like: &%$#!",
            "an html character entity: \xa0",
            "and !",
            "and cats!!! lots and lots of cats!???"]

    TEXT = """This is a multi-line",
              a newline:\n",
              example of text with characters like: &%$#!",
              an html character entity: \xa0",
              and !",
              and cats!!! lots and lots of cats!???"""

    pipeline = [
        remove_blank_elements,
        remove_punctuation,
        remove_html_character_entities,
        remove_newline_chars,
        strip_lines,
        remove_whitespace,
        tokenize]
    result = normalize(TEXT, pipeline)
    print(" ".join(result))
