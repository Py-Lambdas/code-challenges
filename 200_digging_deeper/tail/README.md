# Tail

Make a function that takes a [sequence](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) of items (`items`) (like a list, string, or tuple) and a number (`n`) and returns the last n elements from the given sequence, as a list.

For example:

```python
>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]
>>> tail('hello', 2)
['l', 'o']
>>> tail('hello', 0)
[]
```

Make sure that your function returns an empty list for negative values of n:

```python
>>> tail('hello', -2)
[]
```

## Bonus

As a bonus, refactor your function to work with any [iterable](https://docs.python.org/3/glossary.html#term-iterable), not just [sequences](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range). For example:

```python
>>> squares = (n**2 for n in range(10))
>>> tail(squares, 3)
[49, 64, 81]
```

Some particulars about this new implementation:

- You should make sure you don't loop at all if n is 0 or negative.
- make your function relatively memory efficient (i.e. if you're looping over a very long iterable, don't store the entire thing in memory).

## Hints

- [Getting the last n items from a sequence](https://www.pythonmorsels.com/topics/slicing/)
- [Turning iterables into lists](https://treyhunner.com/2019/05/python-builtins-worth-learning/#list)
- [How to loop over any iterable in Python](https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/#Generators_are_iterators)
- [A data structure that could help with the bonus task](https://pymotw.com/3/collections/deque.html#constraining-the-queue-size)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Feel free to reference the tests if you have any confusion about the expected behavior of the Circle class.

Good luck!
