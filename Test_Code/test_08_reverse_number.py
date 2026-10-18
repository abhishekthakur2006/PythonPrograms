import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
reverse_number = importlib.import_module("Code.08_reverse_number").reverse_number

assert reverse_number(1234) == 4321
assert reverse_number(-508) == -805
assert reverse_number(1200) == 21
assert reverse_number(0) == 0

print("All test cases passed.")