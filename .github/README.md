# Py-Lambdas Code Challenges

> The best way to learn is by doing it!

Welcome to the Py-Lambdas Code Challenges Page.

These are code challenges and mini coding projects created by our Py-Lambdas community.

⚠️ Note: Construction ahead!! This is a work in progress and will be continually updated.

## Q&A

### Why would I use these challenges and not something like LeetCode?

We think that sites like LeetCode, Exercism, HackerRank, etc. have their place; and the thing they're very good at in particular is preparing you for a whiteboarding interview. We're very decidedly _**not**_ providing that service.

We see these challenges as the best way to deepen your Python knowledge specifically, and as a result focus on topics and skills specifically related to being a better _Python_ developer.

If that sounds like something you're interested in, welcome!

### How do I get started?

***NOTE**: If you're an experienced developer and/or have opinions about your preferred text editor and environment management tool, then feel free to skip this section, fork & clone this repository, and get going however you'd like. However, if you're newer to Python, already use VS Code as your preferred editor, and/or just like an automated setup, keep reading.*

We have an automated setup script that will get you started with our recommended environment. It will work on macOS, Windows, and Linux as long as the you've met the following prerequisites:

- You have Python 3 installed on your system and available somewhere in your `$PATH` (e.g. if you run `python --version` in your terminal of choice you get `Python 3.x.x` or something similar)
- You have VS Code installed and the associated `code` command available somewhere in your `$PATH` (i.e. if you run `code --version` you get output of some kind rather than an error).

If you meet both of the above prerequesites, then the process for getting started looks like this:

1. [Fork this repository into your own account](https://github.com//Py-Lambdas/code-challenges/fork). This allows you to commit your solutions and push them to your own repository so you can show off your progress.
2. [Clone the repository to your local computer](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). Generally this is done with `git clone https://github.com/Py-lambdas/code-challenges`, but you can also use the [GitHub CLI](https://cli.github.com/) by running `gh repo:clone Py-lambdas/code-challenges`
3. Navigate your terminal into the `code-challenges` directory. If you're using a *nix shell like bash, zsh, or fish, you'll use the `cd` command to do this (e.g. `cd code-challenges` or `cd path/to/code-challenges`)
4. Run `python3 bin/setup.py` in order to run the installer
5. Open the `code-challenges` repository in VS Code by running `code .` once step 4 completes successfully.

Once you've done this setup process, you can just skip to step 5 every time you want to complete a challenge from then on.

### How do I check my code?

There are a couple ways at your disposal, depending on who you are as a person.

**t3rm1n4l is lyf3 and I think nice things make me weak**:

Within the directory of the specific code challenge you're using, run the following command:

```shell
python -m unittest
```

**I'm ✨fancy✨ and have ✨exquisite✨ taste**:

We have a `launch.json` script that will run python's debugger inside of VS Code.

There are two separate strategies for running it. The first is to create a `if __name__ == '__main__'` block in your python module that tests the code, and then use `breakpoint()` when you'd like to check something. For example if you're creating an `add` function that will add two numbers together, and you want the debugger to pause so you can check what your parameters are every time it runs, you would write the module like so:

```python

def add(x, y):
    breakpoint()
    return x + y

if __name__ == '__main__':
  add(2, 2)
  add(2, 4)
  add('one', 3)
```

To run this in debug mode, you'll go to the debug pane in VS Code (`CMD+SHIFT+D` on macOS, `CTRL+SHIFT+D` on windows), and then select the `Debug module` option in the drop down before clicking the play button.

Alternatively, if you want to run the script in the context of the test inputs, you can add a breakpoint anywhere in your code and then skip to running the debugger _without_ adding a `if __name__ == '__main__'` block by running the `Debug with tests` option in the dropdown.

More information on using VS Code's debugger can be found at the link below:
https://code.visualstudio.com/docs/editor/debugging

### Can I help you out with code reviewing?

Absolutely! All challenges have associated unit tests to check if the code is correct or not. However, we would love any help in manual code review when possible! We want this to be a _community effort_.

### Can I add code challenges?

Yes! Please take a look through [our currently open `challenge:new-addition`) issues](https://github.com/Py-Lambdas/code-challenges/labels/challenge%3Anew-addition) and pick one that you think sounds interesting to work on.

An example of a good challenge to use as a template for now would be the [Circle challenge](https://github.com/Py-Lambdas/code-challenges/tree/master/Circle). Specifically, your new challenge should have:

- An informational `README.md` containing:
  - information about the challenge, and examples of the behavior you'll be testing for.
  - (Optionally) a bonus or two that stretch people to think more pythonically
  - A "Hints" section which links to documentation, articles, videos, and/or particularly informative Stack Overflow answers which provide the knowledge and background necessary to complete the challenge
- A test file
  - tests should be written with `unittest` and not `pytest`. No one should have to pip install anything to complete or test a challenge
  - tests should be documented with docstrings so that people can look over the test file and know which requirement of the challenge each test is checking
  - Optional bonus challenges should have their tests decorated with the `@unittest.expectedFailure` decorator, and a comment telling people know to comment that decorator out if they'd like to attempt the bonus
  - The test file should be named `test_{CHALLENGE_NAME}.py` where `{CHALLENGE_NAME}` is the name of the challenge you're creating.
  - The test file should import the required classes/functions/etc. from the stub file (see below)
- A stub file for the challenge
  - The stub file should be named `{CHALLENGE_NAME}.py` where `{CHALLENGE_NAME}` is the name of the challenge you're creating.
  - The stub file should only contain the absolute minimum and required objects necessary. For example, if your challenge is to create an `add` function that takes two numbers and returns their sum, your stub file should contain `def add(): pass` and the person completing the challenge should be responsible for all other implementation details, including function parameters.
  - If your challenge/your tests do not rely on any required function / class names, your stub file should be empty.

Once you've created a challenge that meets the above structure and performs the way you'd like, make a Pull Request to the [challenges](https://github.com/Py-Lambdas/code-challenges/tree/challenges) branch with any challenges you want to add.

Prior to submitting, please run your code through [black](https://github.com/psf/black) to standardize formatting.

### Can I get help if I am stuck?

Yes! Reach out on Discord for any help you may need!

### What if I find an issue/bug in a challenge?

Submit all issues [here](https://github.com/Py-Lambdas/code-challenges/issues). Issue submissions should include specific filename and the problem. If you have a solution for the bug, include that as well! 😀

## Challenges 🐍

Challenges are organized from Very Easy -> Expert. Within each category, they are in no particular order.

### 100-level: Essentials

This series of challenges is meant to ensure you understand the basics of Python. You may complete them in order, or jump around if there's a particular topic you'd like to challenge yourself on.

|                           name                           |                   topics                   |      author      |
| :------------------------------------------------------: | :----------------------------------------: | :--------------: |
|  [Coordinates](../100_essentials/coordinates/README.md)  |      `variables`, `numbers`, `types`       | @duckeverlasting |
| [Log Transfer](../100_essentials/log_transfer/README.md) | `variables`, `numbers`, `strings`, `types` | @duckeverlasting |
|     [Messages](../100_essentials/messages/README.md)     |         `strings`, `control flow`          |    @brannanc     |
|      [Secrets](../100_essentials/secrets/README.md)      |             `loops`, `strings`             |    @brannanc     |
|    [Greetings](../100_essentials/greetings/README.md)    |  `functions`, `parameters`, `annotations`  |    @brannanc     |
|         [Line](../100_essentials/line/README.md)         |   `classes`, `methods`, `dunder methods`   | @duckeverlasting |
|       [Circle](../100_essentials/Circle/README.md)       | `classes`, `properties`, `dunder methods`  | @nickcannariato  |

### 200-level: Digging Deeper

Now that you've got the essentials of Python under your belt, these challenges are meant to take you on a tour of some of the more commonly seen yet Python-specific features of the language.

|                        name                        |               topics               |     author      |
| :------------------------------------------------: | :--------------------------------: | :-------------: |
|     [add](../200_digging_deeper/add/README.md)     |          `comprehensions`          | @nickcannariato |
| [compact](../200_digging_deeper/compact/README.md) |   `comprehensions`, `generators`   | @nickcannariato |
|    [tail](../200_digging_deeper/tail/README.md)    | `sequences`, `iterators`, `queues` | @nickcannariato |

### 300-level: Peculiarities

Most programming language have opinions that are particular or peculiar, and Python is no exception. Static types vs dynamic types, pass by value or pass by reference, How you should raise and react to errors, etc. These challenges are meant to expose you to those peculiarities and help you think pythonically

|    name     |    topics     |    author    |
| :---------: | :-----------: | :----------: |
| PLACEHOLDER | `PLACEHOLDER` | @PLACEHOLDER |

### 400-level: Paradigm pathways

Python allows for both Object-oriented programming and Functional programming, and these challenges are designed to help you learn how it thinks about both of of those paradigms.

|    name     |    topics     |    author    |
| :---------: | :-----------: | :----------: |
| PLACEHOLDER | `PLACEHOLDER` | @PLACEHOLDER |

### 500-level: The Standard Library

Now that you've got a really good handle on Python's language features, we're gonna give you a detailed tour of Python's Standard Library.

The particular module(s) used by a given challenge will be listed in the `modules` column, which you'll notice has replaced the `topics` column above.

|                           name                           |      modules      |     author      |
| :------------------------------------------------------: | :---------------: | :-------------: |
| [fix_csv](../500_the_standard_library/fix_csv/README.md) | `csv`, `argparse` | @nickcannariato |

### Misc

This `misc` folder of includes more traditional whiteboarding-focused challenges.

As mentioned earlier in this README, this is _not_ the focus of this repository or the challenges we're currently interested in accepting, but we wanted to include them and potentially add to them in the future.
