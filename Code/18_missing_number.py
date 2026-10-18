def find_missing_number(numbers: list[int]) -> int:
    """Find the missing value from a list containing distinct values from 0 to n."""
    count = len(numbers)
    if len(set(numbers)) != count or any(number < 0 or number > count for number in numbers):
        raise ValueError("values must be distinct integers from 0 through the list length")
    return count * (count + 1) // 2 - sum(numbers)


if __name__ == "__main__":
    values = [int(value) for value in input("Enter values from 0 to n, with one missing: ").split()]
    print(find_missing_number(values))