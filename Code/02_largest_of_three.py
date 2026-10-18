def largest_of_three(first: float, second: float, third: float) -> float:
    """Return the largest of three numbers."""
    return max(first, second, third)


if __name__ == "__main__":
    numbers = [float(input(f"Enter number {index}: ")) for index in range(1, 4)]
    print(largest_of_three(*numbers))