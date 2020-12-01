# JS Dict

Create a class called JSDict which creates objects that can use key lookups and attribute lookups interchangeably:

```python
>>> person = JSDict({'name': "Nick Cannariato", 'location': "Fort Worth"})
>>> person.name
'Nick Cannariato'
>>> person['location']
'Fort Worth'
```

At first your object should only worry about accessing keys and attributes and accepting a single dictionary as its one optional argument.

## Bonus 1

For the first bonus, make sure key and attribute assignment to works:

```python
>>> person = JSDict({'name': "Nick Cannariato", 'location': "Fort Worth"})
>>> person.location = "Portland"
>>> person['location']
'Portland'
>>> person['location'] = "Fort Worth"
>>> person.location
'Fort Worth'
```

## Bonus 2

For the second bonus, update your JSDict class to accept keyword arguments, make JSDict objects comparable to each other via equality, and implement a get method that works sort of like the get method on dictionaries:

```python
>>> person = JSDict(name="Nick Cannariato", location="Fort Worth")
>>> person.location
'Fort Worth'
>>> person == JSDict(name="Nick", location="Fort Worth")
False
>>> person == JSDict(name="Nick Cannariato", location="Fort Worth")
True
>>> person.get('profession')
>>> person.get('profession', 'unknown')
'unknown'
>>> person.get('name', 'unknown')
'Nick Cannariato'
```

Bonus 3

For the third bonus, allow your JSDict class to accept a normalize keyword argument which, if true, will "normalize" the spaces in keys to underscores in attributes:

```python
>>> person = JSDict(name="Nick Cannariato", location="Fort Worth", normalize=True)
>>> person['company name'] = "Py Lambdas"
>>> person.company_name
'Py Lambdas'
>>> person['company name']
'Py Lambdas'
```

## Hints

Hints for when you get stuck (hover over links to see what they're about):

- [One way to create a dictionary-like class](https://stackoverflow.com/a/2466232/2633215)
- [How [...] lookups work](https://stackoverflow.com/a/1957793/2633215)
- [Customizing what attribute lookups (obj.thing) do](https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute)
- [Bonus 1: making `x[key] = value` work](https://gist.github.com/turicas/1510860)
- [Bonus 2: keyword-only arguments](https://treyhunner.com/2018/04/keyword-arguments-in-python/#Keyword-only_arguments_without_positional_arguments)
- [Bonus 2: overriding equality between objects](https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes)
- [Bonus 2: the get method](https://docs.python.org/3/library/stdtypes.html#dict.get)
- [Bonus 3: A helper for making dictionary-like classes](https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/#UserList/UserDict:_lists_and_dictionaries_that_are_actually_extensible)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

If you'd like to try the bonus challenges, you'll want to comment out the noted lines of code in the test file to test them properly.

Finally, Feel free to reference the tests if you have any confusion about the expected behavior of the `JSDict` function.

Good luck!
