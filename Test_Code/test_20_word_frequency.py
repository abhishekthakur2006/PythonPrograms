import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
word_frequency = importlib.import_module("Code.20_word_frequency").word_frequency

assert word_frequency("Hello, hello world!") == {"hello": 2, "world": 1}
assert word_frequency("") == {}
assert word_frequency("One-two one.") == {"one": 2, "two": 1}

print("All test cases passed.")