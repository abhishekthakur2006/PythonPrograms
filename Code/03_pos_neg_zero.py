def classify_number(number: float) -> str:
    """Classify a number as positive, negative, or zero."""
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


if __name__ == "__main__":
    value = float(input("Enter a number: "))
    print(classify_number(value))