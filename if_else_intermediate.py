"""
Topic: Intermediate conditional statements example
"""

num = int(input("Enter a number: "))

if num > 0:
    result = "Positive"
elif num < 0:
    result = "Negative"
else:
    result = "Zero"

print("Result:", result)

# Ternary operator example
parity = "Even" if num % 2 == 0 else "Odd"
print("Parity:", parity)