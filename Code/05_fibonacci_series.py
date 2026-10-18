def fibonacci_series(count: int) -> list[int]:
    """Return the first count terms of the Fibonacci sequence."""
    if count < 0:
        raise ValueError("count must be non-negative")
    sequence = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence


if __name__ == "__main__":
    count = int(input("How many terms? "))
    print(fibonacci_series(count))