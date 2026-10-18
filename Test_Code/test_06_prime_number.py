import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
is_prime = importlib.import_module("Code.06_prime_number").is_prime

assert is_prime(2) is True
assert is_prime(17) is True
assert is_prime(1) is False
assert is_prime(0) is False
assert is_prime(-7) is False
assert is_prime(21) is False

print("All test cases passed.")