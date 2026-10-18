def sum_of_digits(number: int) -> int:
    """Return the sum of the digits in an integer's absolute value."""
    return sum(int(digit) for digit in str(abs(number)))


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    print(sum_of_digits(value))