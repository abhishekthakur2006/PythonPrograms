def second_largest(numbers: list[float]) -> float:
    """Return the second-largest distinct number in a non-empty list."""
    distinct_numbers = sorted(set(numbers))
    if len(distinct_numbers) < 2:
        raise ValueError("at least two distinct numbers are required")
    return distinct_numbers[-2]


if __name__ == "__main__":
    numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]
    print(second_largest(numbers))