import pytest
from axentx_product import greet, add, is_palindrome


def test_greet_basic():
    assert greet("World") == "Hello, World!"
    assert greet("") == "Hello, !"


def test_greet_type_error():
    with pytest.raises(TypeError):
        greet(123)  # type: ignore


def test_add_integers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(-0.5, 0.5) == pytest.approx(0.0)


def test_add_type_error():
    with pytest.raises(TypeError):
        add("a", 1)  # type: ignore
    with pytest.raises(TypeError):
        add(1, "b")  # type: ignore


@pytest.mark.parametrize(
    "candidate,expected",
    [
        ("Racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("Hello", False),
        ("", True),
        ("12321", True),
        ("12345", False),
    ],
)
def test_is_palindrome(candidate, expected):
    assert is_palindrome(candidate) == expected


def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(123)  # type: ignore
