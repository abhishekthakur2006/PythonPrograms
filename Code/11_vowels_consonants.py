def count_vowels_consonants(text: str) -> tuple[int, int]:
    """Return the counts of vowels and consonants, ignoring other characters."""
    vowels = 0
    consonants = 0
    for character in text.casefold():
        if character.isalpha():
            if character in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


if __name__ == "__main__":
    text = input("Enter text: ")
    vowels, consonants = count_vowels_consonants(text)
    print(f"Vowels: {vowels}; consonants: {consonants}")