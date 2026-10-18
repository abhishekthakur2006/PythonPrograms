import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
character_frequency = importlib.import_module(
    "Code.14_char_frequency"
).character_frequency

assert character_frequency("banana") == {"b": 1, "a": 3, "n": 2}
assert character_frequency("Aa!") == {"A": 1, "a": 1, "!": 1}
assert character_frequency("") == {}

print("All test cases passed.")