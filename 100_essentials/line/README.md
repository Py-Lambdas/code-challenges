# Line

Create a class that represents a straight line. The class will take in two points as parameters, `point_a` and `point_b`. Points are tuples (x, y) with x and y representing location on a 2d plane.

In Python you can change the string representation of a class. Change the string representation of class `Line` to make it more useful. For instance:

```python
>>> l = Line((4, 8), (-2, 10))
>>> str(l)
'a: (4, 8), b: (-2, 10), distance: 6.32'
```

The class should have methods `translate_x` and `translate_y`. Each method should shift the line a given amount in the x or y direction.

```python
>>> l = Line((4, 8), (-2, 10))
>>> l.translate_x(5)
>>> str(l)
'a: (9, 8), b: (3, 10), distance: 6.32'
```

`line_1` is considered equal to `line_2` if the distance between `line_1`'s points is the same as the distance between `line_2`'s points. Comparisons to anything other than a line should return `False`.

```python
>>> l1 = Line((1, 3), (-2, -4))
>>> l2 = Line((2, 4), (-1, -3))
>>> l1 == l2
True
>>> l3 = Line((4, 3), (1, 5))
>>> l1 == l3
False
```

`line_1` is considered greater than `line_2` if the distance between `line_1`'s points is more than the distance between `line_2`'s points.

```python
>>> l1 = Line((0, 0), (3, 4))
>>> l2 = Line((-1, -1), (4, 5))
>>> l1 < l2
True
```

## Bonus

As a bonus, `Line` should have a `distance` property.

```python
>>> l = Line((4, 8), (-2, 10))
>>> l.distance
6.324555320336759
```


## Hints

- [Classes in python](https://docs.python.org/3/tutorial/classes.html)
- [Classes and Instances in Python](https://www.youtube.com/watch?v=ZDa-Z5JzLYM/)
- [More on classes](https://realpython.com/python3-object-oriented-programming)
- [Special method names (aka dunder methods)](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Understanding `__str__` and `__repr__`](https://medium.com/swlh/string-representations-in-python-understand-repr-vs-str-12f046986eb5)
- [Measuring distance between two points](https://en.wikipedia.org/wiki/Distance#Mathematics)
- [Operator behavior in classes](https://www.tutorialspoint.com/How-to-implement-Python-lt-gt-custom-overloaded-operators)

- [Bonus: property decorators](https://docs.python.org/3/library/functions.html#property)
- [Bonus: making an auto-updating attribute](https://www.youtube.com/watch?v=jCzT9XFZ5bw)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Good luck!

