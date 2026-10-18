import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
classify_number = importlib.import_module("Code.03_pos_neg_zero").classify_number

assert classify_number(4) == "Positive"
assert classify_number(-2.5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number(0.0) == "Zero"

print("All test cases passed.")