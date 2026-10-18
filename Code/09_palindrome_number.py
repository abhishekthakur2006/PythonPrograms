def is_palindrome_number(number: int) -> bool:
    """Return whether a non-negative integer reads the same backward."""
    if number < 0:
        return False
    return number == int(str(number)[::-1])


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    print("Palindrome" if is_palindrome_number(value) else "Not palindrome")