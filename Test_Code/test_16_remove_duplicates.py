import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
remove_duplicates = importlib.import_module("Code.16_remove_duplicates").remove_duplicates

assert remove_duplicates([1, 2, 1, 3, 2]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([4, 4, 4]) == [4]

print("All test cases passed.")