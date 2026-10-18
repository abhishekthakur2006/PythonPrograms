import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
find_duplicates = importlib.import_module("Code.19_find_duplicates").find_duplicates

assert find_duplicates([1, 2, 1, 3, 2, 1]) == [1, 2]
assert find_duplicates([]) == []
assert find_duplicates([4, 5, 6]) == []

print("All test cases passed.")