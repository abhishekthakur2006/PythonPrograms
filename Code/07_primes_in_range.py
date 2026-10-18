def primes_in_range(start: int, end: int) -> list[int]:
    """Return all prime numbers in the inclusive range start to end."""
    primes = []
    for candidate in range(max(2, start), end + 1):
        is_candidate_prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                is_candidate_prime = False
                break
            divisor += 1
        if is_candidate_prime:
            primes.append(candidate)
    return primes


if __name__ == "__main__":
    start = int(input("Start of range: "))
    end = int(input("End of range: "))
    print(primes_in_range(start, end))