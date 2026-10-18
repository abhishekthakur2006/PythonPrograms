def is_prime(number: int) -> bool:
    """Return whether number is a prime integer."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    print("Prime" if is_prime(value) else "Not prime")