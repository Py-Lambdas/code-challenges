# Secrets

You and your friends have come up with a way to write secret messages to each other. Write a function that takes a string and an integer and returns a decoded message.

Each word in the encoded message is separated by a change in case. Also, each character is "shifted" by a given amount. The returned string should be all lowercase.

```python
>>> encoded_message = 'ifmmpXPSME'
>>> secrets(encoded_message, -1)
'hello world'
```

## Hints

- [For statement in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [For loops](https://wiki.python.org/moin/ForLoop)
- [ord and chr functions](https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods)
- [String constants](https://docs.python.org/3.8/library/string.html#module-string)
- [Ascii table](http://www.asciitable.com/)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Good luck!
