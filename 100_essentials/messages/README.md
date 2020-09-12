# Messages

You've written a bunch of messages but you failed to realize that your shift key was broken. Write a function that Capitalizes the first letter of a message.

```python
>>> fix_message('this is a very serious message xoxo')
'This is a very serious message xoxo'
```

For some reason you've signed all your messages with `xoxo`. That's embarrassing. Remove all instances of 'xoxo' from the message.

```python
>>> fix_message('xoxo this is a very serious message xoxo')
'This is a very serious message'
```

Additionally, if the message is an empty string return None.

```python
>>> fix_message('')
None
```

And if the length of the message is over 50 characters, return a message with only the first 50 characters.

```python
>>> msg = "we interrupt this program to annoy you and make things generally more irritating."
>>> fix_message(msg)
'We interrupt this program to annoy you and make th'
```

## Hints

- [Strings introduction](https://docs.python.org/3/tutorial/introduction.html#strings)
- [If, Else and control flow in Python](https://docs.python.org/3/tutorial/controlflow.html)
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Good luck!
