"""Pipeline for gathering usable data from the internet.

Basic Steps
1. Collect URLs using an internet search strategy.
2. Scrape web-pages' text from the URLs using a scrape strategy.
3. Normalize text scraped from the web-pages using a cleaning strategy.
"""

# std lib
from pprint import pprint

# custom
from strategies.web_search import WebSearch, GoogleStrategy
from pipelines.scrapers import  PageScraper, BeautifulSoup
from normalize import  Normalizer, BeautifulSoupNormalizer

if __name__ == "__main__":

    # Search for URls
    google = WebSearch(GoogleStrategy())
    urls = google.search(["I like", "birds"])
#     print(f"URLs:\n{urls}")

    # Scrape web pages from URLs
    scraper = PageScraper(BeautifulSoup())
    text = scraper.scrape(urls[1])
#     print(f"Text:\n{text[:100]}")

    # Normalize content from web pages
    normalizer = Normalizer(BeautifulSoupNormalizer())
    results = normalizer.normalize(text)
#     print(f"Cleaned::\n{cleaned[:100]}")
    
