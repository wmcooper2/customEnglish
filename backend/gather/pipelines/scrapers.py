"""Gather web page content"""

# std lib
from __future__ import annotations
from abc import ABC, abstractmethod
from pprint import pprint
from string import whitespace
from typing import List, Text, Union

# 3rd party
import bs4
import requests


class PageScraper():
    """Scrape content from urls."""

    def __init__(self, strategy: Scraper) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Scraper:
        """Get strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Scraper) -> None:
        self._strategy = strategy

    def scrape(self, url: Text, tag: Text = None) -> None:
        """Calls strategy's scrape() method."""
        return self._strategy.scrape(url, tag)


class Scraper(ABC):
    """Common scraper interface."""

    @abstractmethod
    def scrape(self, url: Text, tag: Text = None):
        """Scrape the url for optional tag."""


class BeautifulSoup(Scraper):
    """Beautiful Soup Scraper."""

    def scrape(self, url: Text, tag: Text = None) -> List[Text]:
        """Scrape the web url for optional tag."""

        soup = self.url_contents(url)
        if tag:
            return self.scrape_for_tags(soup, tag)
        return self.scrape_lines(soup)


    def replace_html_space(self, string: Text) -> Text:
        """Replace HTML character entity non-breaking space with ascii space."""

        return string.replace(u'\xa0', u' ')

    def url_contents(self, url: Text) -> Text:
        """Scrape url for content."""

        req = requests.get(url)
        #print("Kilobytes:", sys.getsizeof(req.text))
        return bs4.BeautifulSoup(req.text, 'html.parser')


    def scrape_text(self, soup: bs4.BeautifulSoup) -> Text:
        """Get only the whitespace stripped text from the soup."""

        return soup.get_text(strip=True)


    def scrape_lines(self, soup: bs4.BeautifulSoup) -> List[Text]:
        """Get the lines of text from the soup."""

        text = soup.get_text()
        return text.split("\n")


    def scrape_for_tags(self, soup: bs4.BeautifulSoup, tag: Text) -> List[Text]:
        """Scrape for tag in soup."""

        return soup.find_all(tag)


if __name__ == "__main__":
    URL = "https://ilikebirds.co.uk/"
    scraper = PageScraper(BeautifulSoup())
    results = scraper.scrape(URL)
    pprint(results[:100])
