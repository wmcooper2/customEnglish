"""Text normalization strategies."""

# std lib
from __future__ import annotations
from abc import ABC, abstractmethod
from pprint import pprint
from string import whitespace
from typing import List, Optional, Text


class Normalizer():
    """Normalize text."""

    def __init__(self, strategy: TextCleaner) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> TextCleaner:
        """Get strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: TextCleaner) -> None:
        self._strategy = strategy

    def normalize(self, lines: List[Text] = None) -> Optional[List[Text]]:
        """Calls strategy's normalize() method."""
        return self._strategy.normalize(lines)


class TextCleaner(ABC):
    """Common TextCleaner interface."""

    @abstractmethod
    def normalize(self, url: Text, tag: Text = None):
        """Normalize the text."""


class BeautifulSoupNormalizer(TextCleaner):
    """Normalize text extracted from Beautiful Soup objects."""

    def normalize(self, lines: List[Text] = None) -> Optional[List[Text]]:

        """Normalize the text."""
        if lines:
            stripped = [line.strip() for line in lines]
            no_blanks = [line for line in stripped if line not in whitespace]
            no_html_spaces = [self._replace_html_space(line) for line in no_blanks]
            return no_blanks
        return None



    def _replace_html_space(self, string: Text) -> Text:
        """Replace HTML character entity non-breaking space with ascii space."""
        return string.replace(u'\xa0', u' ')



if __name__ == "__main__":
    TEXT = ["This is a multi-line",
            "a newline:\n",
            "example of text with characters like: &%$#!",
            "an html character entity: \xa0",
            "and !",
            "and cats!!! lots and lots of cats!???"]
    normalizer = Normalizer(BeautifulSoupNormalizer())
    results = normalizer.normalize(TEXT)
    pprint(results[:100])
