import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
count_vowels_consonants = importlib.import_module(
    "Code.11_vowels_consonants"
).count_vowels_consonants

assert count_vowels_consonants("Hello, World!") == (3, 7)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("123 !") == (0, 0)

print("All test cases passed.")