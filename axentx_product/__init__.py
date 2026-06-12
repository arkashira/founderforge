"""
axentx_product
==============

A minimal utility library that provides a few generic helpers:

* ``greet(name)`` – returns a friendly greeting.
* ``add(a, b)`` – returns the arithmetic sum of two numbers.
* ``is_palindrome(text)`` – checks if a string is a palindrome,
  ignoring case and non‑alphanumeric characters.
"""

from __future__ import annotations

import re
from typing import Any, Union

Number = Union[int, float]


def greet(name: str) -> str:
    """
    Return a friendly greeting for *name*.

    Parameters
    ----------
    name: str
        The name to greet.

    Returns
    -------
    str
        A greeting of the form ``"Hello, <name>!"``.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return f"Hello, {name}!"


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of *a* and *b*.

    The function works with ``int`` and ``float`` values.  If either
    argument is not a number, a ``TypeError`` is raised.

    Parameters
    ----------
    a, b: int | float
        Operands to add.

    Returns
    -------
    int | float
        The arithmetic sum.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an int or float")
    return a + b


def is_palindrome(text: str) -> bool:
    """
    Determine whether *text* is a palindrome.

    The check is case‑insensitive and ignores all characters that are
    not alphanumeric.

    Parameters
    ----------
    text: str
        The string to test.

    Returns
    -------
    bool
        ``True`` if *text* is a palindrome, ``False`` otherwise.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Keep only alphanumeric characters and lower‑case them.
    cleaned = re.sub(r"[^A-Za-z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


__all__ = ["greet", "add", "is_palindrome"]
