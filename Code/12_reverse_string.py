def reverse_string(text: str) -> str:
    """Return text in reverse order without using slicing."""
    characters = []
    for character in text:
        characters.append(character)
    characters.reverse()
    return "".join(characters)


if __name__ == "__main__":
    print(reverse_string(input("Enter text: ")))