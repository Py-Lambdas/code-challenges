# Circle

Create a class that represents a circle.

The circle should have a radius, a diameter, and an area. It should also have a nice string representation.

For example:

```python
>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
```

Additionally the radius should default to 1 if no radius is specified when you create your circle:

```python
>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2
```

Make sure when the radius of your class changes that the diameter and area both automatically update:

```python
>>> c = Circle(2)
>>> c.radius = 1
>>> c.diameter
2
>>> c.area
3.141592653589793
>>> c
Circle(1)
```

You should also be able to set the diameter attribute in your class and have the radius update accordingly.

However, attempting to update the area should raise an `AttributeError`:

```python
>>> c = Circle(1)
>>> c.diameter = 4
>>> c.radius
2.0
>>> c.area = 45.678
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 16, in radius
AttributeError: can't set attribute
```

Finally, a Circle's radius cannot be set to a negative number. If it's attempted, you should raise a `ValueError` exception with the error message `"Radius cannot be negative"`.

```python
>>> c = Circle(5)
>>> c.radius = 3
>>> c.radius = -2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
>>> c = Circle (-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
```

This means that diameter cannot be negative either (and setting diameter to a negative number should also raise a ValueError).

## Hints

- [Formula and background on computing the area of a circle](https://en.wikipedia.org/wiki/Area_of_a_circle)
- [Classes and Instances in Python](https://www.youtube.com/watch?v=ZDa-Z5JzLYM/)
- [Understanding `__str__` and `__repr__`](https://medium.com/swlh/string-representations-in-python-understand-repr-vs-str-12f046986eb5)
- [Python's `math` module: `math.pi`](https://docs.python.org/3/library/math.html#math.pi)
- [Making an auto-updating attribute](https://www.youtube.com/watch?v=jCzT9XFZ5bw)
- [Raising exceptions](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Feel free to reference the tests if you have any confusion about the expected behavior of the Circle class.

Good luck!
