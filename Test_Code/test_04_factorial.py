import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
factorial = importlib.import_module("Code.04_factorial").factorial

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
try:
    factorial(-1)
except ValueError:
    pass
else:
    raise AssertionError("negative input should raise ValueError")

print("All test cases passed.")