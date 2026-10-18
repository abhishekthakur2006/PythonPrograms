import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
fibonacci_series = importlib.import_module("Code.05_fibonacci_series").fibonacci_series

assert fibonacci_series(0) == []
assert fibonacci_series(1) == [0]
assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
try:
    fibonacci_series(-1)
except ValueError:
    pass
else:
    raise AssertionError("negative count should raise ValueError")

print("All test cases passed.")