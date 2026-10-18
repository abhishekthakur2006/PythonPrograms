import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
is_palindrome_string = importlib.import_module(
    "Code.13_palindrome_string"
).is_palindrome_string

assert is_palindrome_string("Racecar") is True
assert is_palindrome_string("A man, a plan, a canal: Panama!") is True
assert is_palindrome_string("Python") is False
assert is_palindrome_string("!!!") is True

print("All test cases passed.")