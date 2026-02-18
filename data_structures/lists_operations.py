"""
List Operations
"""

numbers = [10, 20, 30, 40]

# Add elements
numbers.append(50)
numbers.insert(1, 15)

# Remove element
numbers.remove(30)

# Access elements
first = numbers[0]
last = numbers[-1]

print("Updated list:", numbers)
print("First element:", first)
print("Last element:", last)
print("Elements in list:")
for num in numbers:
    print(num)
