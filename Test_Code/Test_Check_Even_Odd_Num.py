import unittest

from Code.Check_Even_Odd_Num import check_even_odd_num


class TestCheckEvenOddNum(unittest.TestCase):
    def test_even_numbers(self):
        for number in (0, 2, -4):
            with self.subTest(number=number):
                self.assertEqual(check_even_odd_num(number), "Even")

    def test_odd_numbers(self):
        for number in (1, -3):
            with self.subTest(number=number):
                self.assertEqual(check_even_odd_num(number), "Odd")


if __name__ == "__main__":
    unittest.main()
