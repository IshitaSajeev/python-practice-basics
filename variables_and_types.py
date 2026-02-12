"""
Topic: Variables and Data Types
"""

# Basic variables
name = "Alice"
age = 21
height = 5.4
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Type checking
print(type(name), type(age), type(height), type(is_student))

# Dynamic typing demonstration
age = "twenty one"
print("Updated age:", age, type(age))