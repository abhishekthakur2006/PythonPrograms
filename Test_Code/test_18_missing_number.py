import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
find_missing_number = importlib.import_module(
    "Code.18_missing_number"
).find_missing_number

assert find_missing_number([3, 0, 1]) == 2
assert find_missing_number([0]) == 1
assert find_missing_number([]) == 0
for values in ([0, 0], [1, 4]):
    try:
        find_missing_number(values)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid input should raise ValueError")

print("All test cases passed.")