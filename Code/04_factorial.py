def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("factorial is not defined for negative integers")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


if __name__ == "__main__":
    value = int(input("Enter a non-negative integer: "))
    print(factorial(value))