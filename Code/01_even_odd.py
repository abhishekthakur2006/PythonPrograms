def check_even_odd(number: int) -> str:
    """Return whether an integer is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    print(check_even_odd(value))