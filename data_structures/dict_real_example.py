"""
Dictionary Real-World Example.
"""

students = {
    "Riya": {"age": 21, "marks": 85},
    "Rahul": {"age": 22, "marks": 90},
    "Ananya": {"age": 20, "marks": 88}
}

for name, info in students.items():
    print(f"{name} -> Age: {info['age']}, Marks: {info['marks']}")
  
