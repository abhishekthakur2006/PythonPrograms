import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sum_of_digits = importlib.import_module("Code.10_sum_of_digits").sum_of_digits

assert sum_of_digits(12345) == 15
assert sum_of_digits(-908) == 17
assert sum_of_digits(0) == 0

print("All test cases passed.")