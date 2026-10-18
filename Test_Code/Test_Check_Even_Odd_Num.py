import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Code.Check_Even_Odd_Num import check_even_odd_num

assert check_even_odd_num(0) == "Even"
assert check_even_odd_num(2) == "Even"
assert check_even_odd_num(-4) == "Even"
assert check_even_odd_num(1) == "Odd"
assert check_even_odd_num(-3) == "Odd"

print("All test cases passed.")
