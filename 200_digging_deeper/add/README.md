# Add

You'll need to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

```python
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
```

You should solve this problem using only the standard library (e.g. without using a third-party package like `pandas`).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

## Bonus 1

Modify your add function to accept and "add" any number of lists-of-lists. ✔️

```python
>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
```

## Bonus 2

If the arguments provided to the `add` function are different shapes, raise a `ValueError`.

```python
>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
```

## Hints

- [How to loop with and without Indexes in Python](http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/)
- [Using tuple unpacking to improve readability](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/)
- [Python List comprehensions](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)
- [Using `*`'s in Python for packing and unpacking](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_for_packing_arguments_given_to_function)
- [StackOverflow: Raising an exception in Python](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

If you'd like to try the bonus challenges, you'll want to comment out the noted lines of code in the test file to test them properly.

Finally, Feel free to reference the tests if you have any confusion about the expected behavior of the add function.

Good luck!
