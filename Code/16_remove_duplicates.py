def remove_duplicates(numbers: list[int]) -> list[int]:
    """Return the list with duplicates removed, preserving first occurrence order."""
    unique_numbers = []
    seen = set()
    for number in numbers:
        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)
    return unique_numbers


if __name__ == "__main__":
    values = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    print(remove_duplicates(values))