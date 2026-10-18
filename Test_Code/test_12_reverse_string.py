import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
reverse_string = importlib.import_module("Code.12_reverse_string").reverse_string

assert reverse_string("Python") == "nohtyP"
assert reverse_string("") == ""
assert reverse_string("a b!") == "!b a"

print("All test cases passed.")