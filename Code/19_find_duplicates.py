def find_duplicates(numbers: list[int]) -> list[int]:
    """Return each duplicated value once, ordered by its second occurrence."""
    seen = set()
    duplicates = []
    reported = set()
    for number in numbers:
        if number in seen and number not in reported:
            duplicates.append(number)
            reported.add(number)
        seen.add(number)
    return duplicates


if __name__ == "__main__":
    values = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    print(find_duplicates(values))