def is_palindrome_string(text: str) -> bool:
    """Check a string as a case-insensitive sequence of alphanumeric characters."""
    normalized = "".join(character.casefold() for character in text if character.isalnum())
    return normalized == "".join(reversed(normalized))


if __name__ == "__main__":
    value = input("Enter text: ")
    print("Palindrome" if is_palindrome_string(value) else "Not palindrome")