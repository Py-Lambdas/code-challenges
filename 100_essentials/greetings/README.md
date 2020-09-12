# Greetings

Everything you need to complete this challenge can be found [here](https://docs.python.org/3.8/tutorial/controlflow.html#defining-functions).

---

Define a function named `greetings` that takes a required positional argument `name` and a required [key word only](https://docs.python.org/3/glossary.html#term-parameter) argument `punctuation` and returns a greeting in the following format:

```python
>>> greetings('Dave', punctuation='!')
'Hello, Dave!'
```

`greetings` should also take an optional key word argument `msg` that defaults to 'Hello'.

```python
>>> greetings('Mark', msg='Oh, hi', punctuation='!')
'Oh, hi, Mark!'
```

Additionally, `greetings` should take an arbitrary amount of positional arguments to be added as titles in the following format.

```python
>>> greetings('Bob', 'builder', 'tinker', 'tailor', 'soldier', 'spy', msg='Hi', punctuation='.')
'Hi, Bob, the builder, the tinker, the tailor, the soldier, the spy.'
```

`greetings` should also take an arbitrary amount of key word arguments. Each additional key word should be added to the message as `<key> says "<value>".`.

```python
>>> greetings('Dave', msg='Hi', punctuation='!', Mark='Howdy', Jim='You owe me money')
'Hi, Dave! Mark says "Howdy". Jim says "You owe me money".'
```

Add a doc string and annotations to `greetings`. A good doc string might describe what the function does and any inputs and outputs. For parameter and return annotations write a short description for each parameter or use [type hinting](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).

## Hints

- [Parameters in Python](https://docs.python.org/3/glossary.html#term-parameter)
- [Python Docs tutorial section on fuctions](https://docs.python.org/3.8/tutorial/controlflow.html#defining-functions)
- [Variable length arguments in python](https://www.youtube.com/watch?v=kB829ciAXo4)
- [Documenting Python Code](https://realpython.com/documenting-python-code/)
- [Type hint cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Good luck!
