import pytest
from capitalization_and_mutability import *


def test_true():
    assert capitalize_string("hello") == "Hello"
    assert capitalize_string("python") == "Python"
    assert capitalize_string("capital") == "Capital"


def test_false():
    assert capitalize_string("hello") != "hello"
    assert capitalize_string("python") != "python"
    assert capitalize_string("capital") != "capital"
