# LOG TRANSFER

You are working on a program to evaluate bank transactions, and you have been asked to write a function that checks whether an item is a deposit (positive), a withdrawl (negative), or neither. The function should take in a single parameter, `x`, and should return a string decribing the action: `Deposited $[number]`, `Withdrew $[number]`, or `Balance unchanged`.

If `x` is an integer, the number should be kept as is:

```python
>>> log_transfer(24)
"Deposited $24"
>>> log_transfer(-13)
"Withdrew $13"
>>> log_transfer(0)
"Balance unchanged"
```

If `x` is a float, the number should be rounded to two decimal places before it is checked and returned. There's also a specific data type in the standard library that makes this easy and is more commonly used for currency because [floats are funky](https://www.youtube.com/watch?v=PZRI1IfStY0&ab_channel=Computerphile).

```python
>>> log_transfer(499.2543)
"Deposited $499.25"
>>> log_transfer(-43.0387)
"Withdrew $43.04"
```

If `x` is a string, it should be converted to a float, then handled as above.

```python
>>> log_transfer("56.24142")
"Deposited $56.24"
```

## Bonus

As a bonus, if `x` is not a string, int or float, raise a TypeError with the message "x must be a string, int, or float".

If x is an invalid string (doesn't convert to a number), raise a ValueError with a message "x is not a valid number".

```python
>>> log_transfer(True)
TypeError: "x must be a string, int, or float"

>>> log_transfer("a_bunch_of_money")
ValueError: "x is not a valid number"
```

## Hints

- [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Type Function](https://docs.python.org/3/library/functions.html#type)
- [Round Function](https://docs.python.org/3/library/functions.html#round)
- [String Formatting in Python](https://www.w3schools.com/python/ref_string_format.asp)

- [Bonus: Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Bonus: Raising Exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)
- [Bonus: Decimals in Python](https://docs.python.org/3/library/decimal.html)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Good luck!
