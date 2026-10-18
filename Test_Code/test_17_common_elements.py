import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
common_elements = importlib.import_module("Code.17_common_elements").common_elements

assert common_elements([1, 2, 2, 3, 4], [2, 4, 4]) == [2, 4]
assert common_elements([1, 3], [2, 4]) == []
assert common_elements([], [1]) == []

print("All test cases passed.")