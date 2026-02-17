"""
Advanced loop examples using functions and logic
"""

def find_even_numbers(limit):
    evens = []
    for num in range(1, limit + 1):
        if num % 2 == 0:
            evens.append(num)
    return evens

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    try:
        limit = int(input("Enter limit: "))
        print("Even numbers:", find_even_numbers(limit))

        num = int(input("Enter a number for factorial: "))
        print("Factorial:", factorial(num))

    except ValueError:
        print("Please enter valid integers.")