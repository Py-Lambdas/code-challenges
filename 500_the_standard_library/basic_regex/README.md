# Basic Regex

Regular Expressions are used for pattern matching and exist in most programming languages, and all use mostly similar syntax. If words like "Finite State Automata" excite you, then be sure to look into the history and theory of regular expressions. This [computerphile video](https://www.youtube.com/watch?v=528Jc3q86F8) isn't confusing at all.

The [re Module](https://docs.python.org/3/library/re.html) should be used to complete all of the following tasks.

Recently, you've been reaching out to a lot of people over social media and at the end of the conversation you always like to thank them for their time and leave them with your email address. But after reviewing past conversations, you realize you've made some embarassing mistakes. Write a function to prevent any further embarassment.

<!-- Contains name -->

Oh my goodness, you wrote the wrong name in some of your messages, how embarassing. Write a function that takes a sentence and a name as parameters, and returns `True` if the given name is in the sentence, and otherwise returns `False`.

```python
>>> sentence = 'Thanks so much for listening to my nonsense, Rachel!'
>>> name = 'Rachel'
>>> is_valid_send_off(sentence, name)
True
```

<!-- Is it a sentence pattern = r"^[A-Z][^.?!]*[.?!]$" -->

Oh, wow, your grammar is bad. At least make sure the sentence starts with a capital letter and ends with puncuation.

```python
>>> sentence = 'thanks so much for listening to my nonsense, Rachel!'
>>> name = 'Rachel'
>>> is_valid_send_off(sentence, name)
False
```

<!-- Contains email -->

You forgot to leave them your email, again... Check whether the sentence contains a valid email address.

```python
>>> sentence = 'Thanks so much for listening to my nonsense, Rachel!'
>>> name = 'Rachel'
>>> is_valid_send_off(sentence, name)
False
>>> sentence = "Thanks, Rachel, you can reach me at realemail@notfake.net and let's chat again soon!"
>>> name = 'Rachel'
>>> is_valid_send_off(sentence, name)
True
```

## Bonus

The bonus challenge is trickier email validation. Good luck. In addition, here's some suggestions for extra practice.

- [HackerRank](https://www.hackerrank.com/domains/regex)
- [CodeSignal](https://app.codesignal.com/interview-practice/topics/regex)

## Hints

- [Real Python regex tutorial](https://realpython.com/regex-python/)
- [pythex regex checker](https://pythex.org/)
- [Python Docs HOWTO](https://docs.python.org/3/howto/regex.html)
- [Python Docs re Module](https://docs.python.org/3/library/re.html)

## Tests

Move your terminal to the directory that contains this README and then run `python -m unittest` to run the tests for this challenge.

Finally, if you'd like to try the bonus challenge, you'll want to uncomment the bonus function in the test file to test it properly.

Good luck!
