import re


def word_frequency(sentence: str) -> dict[str, int]:
    """Count case-insensitive words, ignoring punctuation."""
    frequencies = {}
    for word in re.findall(r"\b\w+\b", sentence.casefold()):
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


if __name__ == "__main__":
    print(word_frequency(input("Enter a sentence: ")))