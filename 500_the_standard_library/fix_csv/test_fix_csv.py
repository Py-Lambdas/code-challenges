from contextlib import contextmanager, redirect_stderr, redirect_stdout
from io import StringIO
from importlib.machinery import SourceFileLoader
import os
import sys
import warnings
import shlex
from textwrap import dedent
from tempfile import NamedTemporaryFile
import unittest


class FixCSVTests(unittest.TestCase):
    maxDiff = None

    def test_pipe_file_to_csv_file(self):
        old_contents = dedent(
            """
            2012|Lexus|LFA
            2009|GMC|Yukon XL 1500
            1965|Ford|Mustang
            2005|Hyundai|Sonata
            1995|Mercedes-Benz|C-Class
        """
        ).lstrip()

        expected = dedent(
            """
            2012,Lexus,LFA
            2009,GMC,Yukon XL 1500
            1965,Ford,Mustang
            2005,Hyundai,Sonata
            1995,Mercedes-Benz,C-Class
        """
        ).lstrip()

        with make_file(old_contents) as old, make_file("") as new:
            output = run_program(f"fix_csv.py {old} {new}")
            with open(new) as new_file:
                new_contents = new_file.read()

        self.assertEqual(expected, new_contents)
        self.assertEqual("", output)

    def test_delimiter_in_output(self):
        old_contents = dedent(
            """
            02|Waylon Jennings|Honky Tonk Heroes (Like Me)
            04|Kris Kristofferson|To Beat The Devil
            11|Johnny Cash|Folsom Prison Blues
            13|Billy Joe Shaver|Low Down Freedom
            21|Hank Williams III|Mississippi Mud
            22|David Allan Coe|Willie, Waylon, And Me
            24|Bob Dylan|House Of The Risin' Sun
        """
        ).lstrip()

        expected = dedent(
            """
            02,Waylon Jennings,Honky Tonk Heroes (Like Me)
            04,Kris Kristofferson,To Beat The Devil
            11,Johnny Cash,Folsom Prison Blues
            13,Billy Joe Shaver,Low Down Freedom
            21,Hank Williams III,Mississippi Mud
            22,David Allan Coe,"Willie, Waylon, And Me"
            24,Bob Dylan,House Of The Risin' Sun
        """
        ).lstrip()

        with make_file(old_contents) as old, make_file("") as new:
            output = run_program(f"fix_csv.py {old} {new}")
            with open(new) as new_file:
                new_contents = new_file.read()

        self.assertEqual(expected, new_contents)
        self.assertEqual("", output)

    def test_original_file_is_unchanged(self):
        old_contents = dedent(
            """
            2012|Lexus|LFA
            2009|GMC|Yukon XL 1500
        """
        ).lstrip()

        with make_file(old_contents) as old, make_file("") as new:
            run_program(f"fix_csv.py {old} {new}")
            with open(old) as old_file:
                contents = old_file.read()

        self.assertEqual(old_contents, contents)

    def test_call_with_too_many_files(self):
        with make_file("") as old, make_file("") as new:
            with self.assertRaises(BaseException):
                run_program(f"fix_csv.py {old} {new} {old}")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_in_delimiter_and_in_quote(self):
        old_contents = dedent(
            """
            2012 Lexus "LFA"
            2009 GMC 'Yukon XL 1500'
            1995 "Mercedes-Benz" C-Class
        """
        ).lstrip()

        expected1 = dedent(
            """
            2012,Lexus,LFA
            2009,GMC,'Yukon,XL,1500'
            1995,Mercedes-Benz,C-Class
        """
        ).lstrip()

        expected2 = dedent(
            '''
            2012,Lexus,"""LFA"""
            2009,GMC,Yukon XL 1500
            1995,"""Mercedes-Benz""",C-Class
        '''
        ).lstrip()

        with make_file(old_contents) as old, make_file("") as new:
            run_program(f'fix_csv.py {old} {new} --in-delimiter=" "')
            with open(new) as new_file:
                self.assertEqual(expected1, new_file.read())

            run_program(f"""fix_csv.py --in-delimiter=" " --in-quote="'" {old} {new}""")
            with open(new) as new_file:
                self.assertEqual(expected2, new_file.read())

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_autodetect_input_format(self):
        contents1 = dedent(
            """
            '2012' 'Lexus' 'LFA'
            '2009' 'GMC' 'Yukon XL 1500'
            '1995' 'Mercedes-Benz' 'C-Class'
        """
        ).lstrip()

        expected1 = dedent(
            """
            2012,Lexus,LFA
            2009,GMC,Yukon XL 1500
            1995,Mercedes-Benz,C-Class
        """
        ).lstrip()

        with make_file(contents1) as old, make_file("") as new:
            run_program(f"fix_csv.py {old} {new}")
            with open(new) as new_file:
                self.assertEqual(expected1, new_file.read())

        contents2 = dedent(
            """
            "02"\t"Waylon Jennings"\t"Honky Tonk Heroes (Like Me)"\t"3:29"
            "04"\t"Kris Kristofferson"\t"To Beat The Devil"\t"4:05"
            "11"\t"Johnny Cash"\t"Folsom Prison Blues"\t"2:51"
            "13"\t"Billy Joe Shaver"\t"Low Down Freedom"\t"2:53"
            "21"\t"Hank Williams III"\t"Mississippi Mud"\t"3:32"
            "22"\t"David Allan Coe"\t"Willie, Waylon, And Me"\t"3:24"
            "24"\t"Bob Dylan"\t"House Of The Risin' Sun"\t"5:20"
        """
        ).lstrip()

        expected2 = dedent(
            """
            02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
            04,Kris Kristofferson,To Beat The Devil,4:05
            11,Johnny Cash,Folsom Prison Blues,2:51
            13,Billy Joe Shaver,Low Down Freedom,2:53
            21,Hank Williams III,Mississippi Mud,3:32
            22,David Allan Coe,"Willie, Waylon, And Me",3:24
            24,Bob Dylan,House Of The Risin' Sun,5:20
        """
        ).lstrip()

        with make_file(contents2) as old, make_file("") as new:
            run_program(f"fix_csv.py {old} {new}")
            with open(new) as new_file:
                self.assertEqual(expected2, new_file.read())


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(arguments="", raises=DummyException):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.
    """
    arguments = arguments.replace("\\", "\\\\")
    path, *args = shlex.split(arguments)
    old_args = sys.argv
    warnings.simplefilter("ignore", ResourceWarning)

    try:
        sys.argv = [path] + args

        try:
            if "__main__" in sys.modules:
                del sys.modules["__main__"]

            with redirect_stdout(StringIO()) as output:
                with redirect_stderr(output):
                    SourceFileLoader("__main__", path).load_module()
        except raises:
            return output.getvalue()
        except SystemExit as e:
            if e.args != (0,):
                raise SystemExit(output.getvalue()) from e
        finally:
            sys.modules.pop("__main__", None)

        if raises is not DummyException:
            raise AssertionError("{} not raised".format(raises))

        return output.getvalue()
    finally:
        sys.argv = old_args


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode="wt", encoding="utf-8", delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
