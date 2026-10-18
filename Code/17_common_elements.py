def common_elements(first: list[int], second: list[int]) -> list[int]:
    """Return unique common values in the order they first appear in first."""
    second_values = set(second)
    common = []
    seen = set()
    for value in first:
        if value in second_values and value not in seen:
            common.append(value)
            seen.add(value)
    return common


if __name__ == "__main__":
    first = [int(value) for value in input("First list: ").split()]
    second = [int(value) for value in input("Second list: ").split()]
    print(common_elements(first, second))