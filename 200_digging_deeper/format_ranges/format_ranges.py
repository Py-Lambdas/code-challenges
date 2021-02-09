from typing import Iterable


def format_ranges(numbers: Iterable[int]) -> str:
    """
    Given an iterable of numbers, return a string that groups ranges of consecutive numbers together

    >>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
    '1-3,5-8,10-11'
    >>> format_ranges(n+1 for n in numbers)
    '4-5,16-18,20-21'
    """
    pass
