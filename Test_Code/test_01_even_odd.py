import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
check_even_odd = importlib.import_module("Code.01_even_odd").check_even_odd

assert check_even_odd(0) == "Even"
assert check_even_odd(8) == "Even"
assert check_even_odd(-4) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(-3) == "Odd"

print("All test cases passed.")