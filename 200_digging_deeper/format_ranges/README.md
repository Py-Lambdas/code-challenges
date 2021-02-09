# format_ranges

Write a function format_ranges, that takes a list of numbers and returns a string that groups ranges of consecutive numbers together:

```python
>>> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
'1-8'
>>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
'1-3,5-8,10-11'
```

The function should accept other iterables also not just lists:

```python
>>> numbers = [3, 4, 15, 16, 17, 19, 20]
>>> format_ranges(n+1 for n in numbers)
'4-5,16-18,20-21'
```

All runs of consecutive numbers will be collapsed into N-M ranges where N is the start of the consecutive range and M is the end.

This is sort of like the format that printers use for choosing which pages to print.

At first you can assume that all consecutive ranges of numbers will be at least 2 consecutive numbers long.

## Bonus 1

Update your function to handle ranges of individual numbers by representing them as a single number:

```python
>>> format_ranges([4])
'4'
>>> format_ranges([1, 3, 5, 6, 8])
'1,3,5-6,8'
```

## Bonus 2

Update your function so that it works even if the provided iterable of numbers is unordered:

```python
>>> format_ranges([9, 1, 7, 3, 2, 6, 8])
'1-3,6-9'
```

## Bonus 3

Finally, update your function so that it handles duplicate numbers specially. Whenever a number occurs more than once, it should be considered as part of a separate range of numbers.

```python
>>> format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7])
'1-2,1-4,4,7,7-9'
>>> format_ranges([1, 3, 5, 6, 8])
'1,3,5-6,8'
```

The ranges should always be ordered by the lowest start number and then shortest range (when the start numbers are the same).

## Hints

- [Identifying groups of consecutive integers](https://stackoverflow.com/a/2154741/2633215)
- [Converting a list of integers into a string](https://stackoverflow.com/a/28883101/2633215)
- [A one-liner for checking a condition](https://stackoverflow.com/a/394814/2633215)
- [Counting the occurrences of numbers](https://stackoverflow.com/a/23241146/2633215)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Feel free to reference the tests if you have any confusion about the expected behavior.

Good luck!
