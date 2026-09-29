# Python - Safe Functions & Unbreakable

## Files
- `safe_tools.py` - Three crash-proof functions: `safe_divide(a, b)`, `safe_number(text)`, and `get_field(learner, key)`, each using `try` / `except` to return a friendly message instead of raising an error.
- `unbreakable.py` - A program that asks the user for a number and refuses to crash, no matter what they type, using `try` / `except` inside a loop.

## Reflection
An `if` check cannot catch `"abc"` on its own because the problem is not
something you can test for with a simple comparison - `int("abc")` fails the
moment Python tries to convert it, and by then it is too late to prevent the
crash. Only `try` / `except` lets you attempt the conversion and recover
cleanly when the `ValueError` is raised.
