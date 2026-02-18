"""
List Comprehension
"""

numbers = list(range(1, 11))

# Squares of numbers
squares = [n**2 for n in numbers]

# Even numbers
evens = [n for n in numbers if n % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", evens)
