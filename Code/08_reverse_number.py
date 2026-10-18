def reverse_number(number: int) -> int:
    """Return the number with its digits reversed, preserving its sign."""
    reversed_digits = int(str(abs(number))[::-1])
    return -reversed_digits if number < 0 else reversed_digits


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    print(reverse_number(value))