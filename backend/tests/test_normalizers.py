"""Normalizers Unit Tests."""

# stdlib
import re
import sqlite3

# 3rd party
import pytest

@pytest.fixture
def html_chars_regex():
    return re.compile(r"(&#\d*?;)|(&\w*?;)")

@pytest.fixture
def html_chars():
    return r"""&nbsp;&#160;&lt;&#60;&gt;&#62;&amp;&#38;&quot;&#34;&apos;	&#39;&cent;&#162;&pound;&#163;&yen;&#165;&euro;&#8364;&copy;&#169;&reg;	&#174;"""


def test_remove_html_character_entities(html_chars_regex, html_chars):
    # basically means it works if its 2 tabs
    assert html_chars_regex.sub("", html_chars) == "\t\t"


