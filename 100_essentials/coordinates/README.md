# COORDINATES

Find the slope of two coordinate pairs, and then find a third coordinate on the same slope.

A company is building a series of sunglass bodegas in town and they have determined that the bodegas should be in a roughly straight line, for some reason. The town is divided into blocks, each of which can be definined by a set of two integers, `x` and `y`. Find the slope between two already existing bodegas, and use it to find the best location for a third, given the `x` coordinate.

Declare a series of integers `x1`, `y1`, `x2`, and `y2`.

- `x1` should equal 0
- `y1` should equal 4
- `x2` should equal 6
- `y2` should equal 11

Declare a variable `slope`. Slope should equal the slope from (x1, y1) to (x2, y2).

Declare a third pair of coordinates, `x3` and `y3`.

- `x3` should equal 14
- `y3` should equal the *closest integer* along the line formed by the first two pairs of coordinates.

## Hints

- [Numeric Types in Python](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- The slope of a line given two pairs of coordinates is `(y2 - y1) / (x2 - x1)`.
- The equation of a line is `y = slope * x + y_intercept` (The y_intercept is the value of y when x is equal to 0).
- [Linear Equations](https://en.wikipedia.org/wiki/Linear_equation)
- [Rounding in Python](https://docs.python.org/3/library/functions.html#round)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Good luck!
