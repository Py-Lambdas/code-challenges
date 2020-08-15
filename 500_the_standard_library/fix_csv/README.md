# Fix CSVs

You're going to write a basic command line program to normalize CSV files, named `fix_csv.py`. The CLI will turn a pipe-delimited file into a comma-delimited file. You'll see how that will work below.

An original, pipe-delimited file would look something like this:

```csv
Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
```

And you would run that file through your command-line program typing this in your terminal:

```shell
python fix_csv.py cars-original.csv cars.csv
```

As you can see above, `fix_csv.py` takes the path of the pipe-delimited file as its first argument, and the path to the location you'd like your fixed file to be created as the second argument.

Your fixed file should then look like this:

```csv
Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
```

Some important things to note:
- It's valid for a comma to be in your input data, but you'll need to surround data cells with commas in them by double quotes when writing your output file.
- It's also valid for a quote character to be in your input (you'll need to double up quotes because [that's how CSV escaping works](https://stackoverflow.com/questions/17808511/properly-escape-a-double-quote-in-csv).

See the hints if you need help working with CSV files in Python.

## Bonus 1

Now that you've passed MVP, refactor your program to allow the input delimiter and quote character (`"`) by default) to be optionally specified.

For example any of these should work (all specify input delimiter as pipe and the last two additionally specifies the quote character as single quote):

```shell
$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="|" --in-delimiter="," cars.csv cars-fixed.csv
```

To do this, you'll need to look into parsing command-line arguments with Python. There are some standard library modules that can help you out with this. There are 3 different solutions in the standard library actually, but only one I'd recommend.

Once again, avoid `pip install`-ing anything to complete this challenge. These challenges are meant to increase your understanding of Python itself.

Be sure to really read the docs on [Python's CSV module](https://docs.python.org/3/library/csv.html), or you might end up re-implementing a lot of functionality that Python gives you for free.

## Bonus 2

Try to automatically detect the delimiter if an in-delimiter value isn't supplied (don't assume it's pipe and quote, try to get your program to intelligently figure it out).

This is a bit trickier and your solution will likely not work correctly for all files. Definitely check the hints on this one if you get stuck.

## Hints

- [Using `sys.argv` to access command line arguments](https://stackoverflow.com/a/35421024/2633215)
- [Example usage of the `csv` module in the standard library](https://pymotw.com/3/csv/index.html)
- [Corey Shafer's short `csv` module tutorial](https://www.youtube.com/watch?v=q5uM4VKywbA)
- [Restricting the number of command line arguments with multiple assignment](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/#Multiple_assignment_is_very_strict)
- [Using `argparse` to parse command line arguments and flags](http://zetcode.com/python/argparse/)
- [This could be useful to intelligently figure out how to parse a csv file...](https://docs.python.org/3/library/csv.html#csv.Sniffer)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

You'll notice that there are no CSV files in this directory, and that's on purpose. If you examine the tests, you'll see that I'm generating files when you run the tests and then cleaning them up afterwards.

You're welcome to create your own test CSV files if you want to run it yourself with your own data, but the test file itself should be enough to run your solution through its paces.

Finally, if you'd like to try the bonus challenges, you'll want to comment out the noted lines of code in the test file to test them properly.

Good luck!
