"""
Advanced conditional statements using functions and error handling
"""

def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def check_parity(num):
    return "Even" if num % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))

        print("Result:", classify_number(num))
        print("Parity:", check_parity(num))

    except ValueError:
        print("Please enter a valid integer.")