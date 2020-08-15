"""
Challenge: Correct a function that takes a string and returns the first character capitalized in the string.
Difficulty: Easy

Examples:
capitalize_word("hello") ➞ "Hello"
capitalize_word("i") ➞ "I"
capitalize_word("lambda") ➞ "Lambda"

Author: @joshrutkowski
"""


def capitalize_string(word):
    return "".join(char.isupper() for char in word)

