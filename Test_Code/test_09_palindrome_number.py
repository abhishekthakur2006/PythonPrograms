import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
is_palindrome_number = importlib.import_module("Code.09_palindrome_number").is_palindrome_number

assert is_palindrome_number(121) is True
assert is_palindrome_number(0) is True
assert is_palindrome_number(123) is False
assert is_palindrome_number(-121) is False

print("All test cases passed.")