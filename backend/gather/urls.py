"""Gather URLs from various search engines."""

# std lib
from collections import namedtuple
import sys
from typing import List, Text, Union

# 3rd party
from bs4 import BeautifulSoup
import requests

Context = namedtuple("Context", ["grammar", "subject"])



#TODO, convert to Strategy Pattern
def search_google(query: Union[Context, Text]) -> List[Text]:
    """Search Google for 'query'."""

    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
     
    urls = set()
    print("is Context?:", isinstance(query, Context))
    if isinstance(query, Context):
        for url in search(f"{query.grammar} {query.subject}", tld="com", num=10, stop=10, pause=2):
#            print(url)
            urls.add(url)
    else:
        for url in search(query, tld="com", num=10, stop=10, pause=2):
#            print(url)
            urls.add(url)

    return urls

def web_page(url: Text) -> Text:
    """Scrape web page content."""
    req = requests.get(url)
    print("Kilobytes:", sys.getsizeof(req.text))
#    soup = BeautifulSoup(req, 'html.parser')




if __name__ == "__main__":
    query = "birds"
    urls = search_google(query)
    print(f"Search {query}:",urls)

    #query = Context("like", "birds")
    #urls = search_google(query)
    #print(f"Search {query}:",urls)

    for url in list(urls)[:1]:
        web_page(url)
        #scrape urls
