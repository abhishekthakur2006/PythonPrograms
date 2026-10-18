import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
largest_of_three = importlib.import_module("Code.02_largest_of_three").largest_of_three

assert largest_of_three(1, 2, 3) == 3
assert largest_of_three(9, 4, 2) == 9
assert largest_of_three(-1, -8, -3) == -1
assert largest_of_three(5, 5, 2) == 5

print("All test cases passed.")