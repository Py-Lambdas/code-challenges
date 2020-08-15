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

Fork this repository and start coding away!🚀 Test your solution by running the associated unit test. When you are reading to submit, submit a Pull Request to the [submissions](https://github.com/Py-Lambdas/code-challenges/tree/submissions) branch with your solution.

### How do I check my code?

Within the directory of your code challenge, run the following command for unit testing:

```shell
python -m unittest
```

### Can I help you out with code reviewing?

Absolutely! All challenges have associated unit tests to check if the code is correct or not. However, we would love any help in manual code review when possible! We want this to be a _community effort_.

### Can I add code challenges?

Yes! Please take a look through [our currently open `challenge:new-addition`) issues](https://github.com/Py-Lambdas/code-challenges/labels/challenge%3Anew-addition) and pick one that you think sounds interesting to work on.

An example of a good challenge to use as a template for now would be the [Circle challenge](https://github.com/Py-Lambdas/code-challenges/tree/master/Circle). SpecificA ally, your new challenge should have:

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

|             name              |                  topics                   |     author      |
| :---------------------------: | :---------------------------------------: | :-------------: |
| [Circle](../Circle/README.md) | `classes`, `properties`, `dunder methods` | @nickcannariato |


### 200-level: Digging Deeper

Now that you've got the essentials of Python under your belt, these challenges are meant to take you on a tour of some of the more commonly seen yet Python-specific features of the language.

|             name              |                  topics                   |     author      |
| :---------------------------: | :---------------------------------------: | :-------------: |
| [Circle](../Circle/README.md) | `classes`, `properties`, `dunder methods` | @nickcannariato |

### 300-level: Peculiarities

Most programming language have opinions that are particular or peculiar, and Python is no exception. Static types vs dynamic types, pass by value or pass by reference, How you should raise and react to errors, etc. These challenges are meant to expose you to those peculiarities and help you think pythonically

|             name              |                  topics                   |     author      |
| :---------------------------: | :---------------------------------------: | :-------------: |
| [Circle](../Circle/README.md) | `classes`, `properties`, `dunder methods` | @nickcannariato |

### 400-level: Paradigm pathways

Python allows for both Object-oriented programming and Functional programming, and these challenges are designed to help you learn how it thinks about both of of those paradigms.

|             name              |                  topics                   |     author      |
| :---------------------------: | :---------------------------------------: | :-------------: |
| [Circle](../Circle/README.md) | `classes`, `properties`, `dunder methods` | @nickcannariato |

### 500-level: The Standard Library

Now that you've got a really good handle on Python's language features, we're gonna give you a detailed tour of Python's Standard Library. 

The particular module(s) used by a given challenge will be listed in the `modules` column, which you'll notice has replaced the `topics` column above.

|             name              |                  topics                   |     author      |
| :---------------------------: | :---------------------------------------: | :-------------: |
| [Circle](../Circle/README.md) | `classes`, `properties`, `dunder methods` | @nickcannariato |

### Misc

This `misc` folder of includes more traditional whiteboarding-focused challenges. 

As mentioned earlier in this README, this is _not_ the focus of this repository or the challenges we're currently interested in accepting, but we wanted to include them and potentially add to them in the future.
