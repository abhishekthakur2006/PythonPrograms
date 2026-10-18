import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
second_largest = importlib.import_module("Code.15_second_largest").second_largest

assert second_largest([1, 3, 2]) == 2
assert second_largest([5, 5, 4]) == 4
assert second_largest([-1, -3, -2]) == -2
for values in ([], [7, 7]):
    try:
        second_largest(values)
    except ValueError:
        pass
    else:
        raise AssertionError("fewer than two distinct values should raise ValueError")

print("All test cases passed.")