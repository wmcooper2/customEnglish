"""Web Searching Strategies."""

# std lib
from __future__ import annotations
from abc import ABC, abstractmethod
from collections import namedtuple
import functools
from pprint import pprint
from typing import List, Text

# 3rd party
import bs4
import requests
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


Context = namedtuple("Context", ["grammar", "subject"])


class WebSearch():
    """Search the Web"""

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """Get strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Set strategy."""
        self._strategy = strategy

    def search(self, query: List[Text]) -> None:
        """Calls strategy's search() method."""
        return self._strategy.search(query)


class Strategy(ABC):
    """Common search interface."""

    @abstractmethod
    def search(self, query: List[Text]):
        """Start the internet search."""


class GoogleStrategy(Strategy):
    """Perform Web search using Google."""

    def search(self, query: List[Text]) -> List[Text]:
        """Search Google for 'query'."""
        assert isinstance(query, list), "Search query must be a list of strings."

        urls = set()
        if isinstance(query, List):
            search_string = functools.reduce(lambda x, y: f"{x} {y}", query)
            for url in search(search_string, tld="com", num=10, stop=10, pause=2):
                urls.add(url)
        else:
            for url in search(query, tld="com", num=10, stop=10, pause=2):
                urls.add(url)

        return list(urls)


class StrategyTemplate(Strategy):
    """Template... change to whatever strategy."""

    def search(self, query: List[Text]) -> List:
        return f"Template search for: {query}"



if __name__ == "__main__":

    print("="*9, __file__)
    google = WebSearch(GoogleStrategy())
    # res = google.search(Context("I like", "birds"))
    res = google.search(["I like", "birds"])
    pprint(res)
