import pytest
from alphabet_soup import *


def test():
    assert alphabet_soup("hello") == "ehllo"
    assert alphabet_soup("edabit") == "abdeit"
    assert alphabet_soup("hacker") == "acehkr"
    assert alphabet_soup("geek") == "eegk"
    assert alphabet_soup("javascript") == "aacijprstv"
    assert alphabet_soup("credibility") == "bcdeiiilrty"
    assert alphabet_soup("apostrophe") == "aehoopprst"
    assert alphabet_soup("determination") == "adeeiimnnortt"
    assert alphabet_soup("win") == "inw"
    assert alphabet_soup("synthesis") == "ehinsssty"

