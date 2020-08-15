# Compact

Write a function that accepts a sequence (a `list` for example) and returns a new iterable (anything you can loop over) with **adjacent** duplicate values removed.

For example:

```python
>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]
```

There are two bonuses for this exercise.

I recommend solving the exercise without the bonuses first and then attempting each bonus separately.

## Bonus 1

Refactor the `compact` function to accept any iterable, not just a sequence (which means you can't use index look-ups in your answer).

Here's an example with a generator expression, which is a lazy iterable:

```python
>>> compact(n**2 for n in [1, 2, 2])
[1, 4]
```

## Bonus 2

Refactor the `compact` function once more to return an iterator instead of a `list`.

```python
>>> c = compact(n**2 for n in [1, 2, 2])
>>> iter(c) is c
True
```

This should allow your compact function to accept iterables that are theoretically infinite in length (or other lazy iterables).

## Hints

- [The Pythonic way to loop with indexes in Python (i.e. _stop using `range`_)](https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/)
- [How to create iterators in Python](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/)
- [**Only read this if you've completed the challenge + bonuses**: An interesting solution using the standard library](https://stackoverflow.com/questions/41511555/fast-removal-of-consecutive-duplicates-in-a-list-and-corresponding-items-from-an/41511571#41511571)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

If you'd like to try the bonus challenges, you'll want to comment out the noted lines of code in the test file to test them properly.

Finally, Feel free to reference the tests if you have any confusion about the expected behavior of the add function.

Good luck!
