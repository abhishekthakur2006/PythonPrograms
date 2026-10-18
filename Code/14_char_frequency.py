def character_frequency(text: str) -> dict[str, int]:
    """Return the case-sensitive frequency of each character in text."""
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1
    return frequencies


if __name__ == "__main__":
    print(character_frequency(input("Enter text: ")))