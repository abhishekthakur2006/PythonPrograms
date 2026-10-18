import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
primes_in_range = importlib.import_module("Code.07_primes_in_range").primes_in_range

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(14, 20) == [17, 19]
assert primes_in_range(-5, 2) == [2]
assert primes_in_range(10, 1) == []

print("All test cases passed.")