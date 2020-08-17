# Greetings

Define a function named `greet` that takes in a name and a message as inputs and returns a greeting in the following format:

```python
>>> greet("Mark", "Oh, hi")
'Oh, hi, Mark!'
```

Additionally, the message should default to "Hello" if none is provided.

```python
>>> greet("Dave")
'Hello, Dave!'
```

Function arguments can also be functions. Define a function named `greet_with_style` that takes a name as a positional argument, plus an arbitrary number of functions, an optional kew word parameter named `msg` that defaults to 'Hello', another key word argument named `sep` that defaults to ', ', and a required keyword parameter named `punctuation`. `greet_with_style` should return a greeting (name + sep + message + puncuation) with all functions applied to it.

```python
>>> def starify(s):
...    return "*".join(list(s))
>>> greet_with_style("Citizen", "Hello", starify, puncuation="!", sep='*' shout=True)
'C*I*T*I*Z*E*N***H*E*L*L*O*!'
```

- add_epitaphs(name, \*\*kwargs)
- Doc strings and annotations - add to greet_with_style

```python
# TESTS
greet_with_style("Citizen", "Hello", starify, puncuation="!", sep='*' shout=True)
'C*I*T*I*Z*E*N***H*E*L*L*O!'

greet_with_style(add_epitaphs("Citizen", **epitaphs), puncuation="!", shout=True)
"HELLO, CITIZEN, SON OF GREG, LEADER OF KOBOLDS!"
```

- bonus: positional only? What's a use case for positional only (a,b,/,x,y)?
- bonus: functions can return functions
- bonus: decorators example: trace, challenge: write partial apply

- Hint: Example of a function named hello_world that has no inputs and returns the string "Hello world!", https://docs.python.org/3.8/tutorial/controlflow.html#defining-functions
- Hint: Example of using \*args as a list of functions
