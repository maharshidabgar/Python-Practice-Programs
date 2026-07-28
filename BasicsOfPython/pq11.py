"""
===========================================================
🐍 Python Practice Question #11

Question:
Write a Python program to:
1. Count the number of times the grade 'A' appears in a
   tuple.
2. Sort a list of grades in ascending order and display the
   sorted list.

Objective:
- Learn how to work with tuples and lists.
- Count the occurrence of an element in a tuple.
- Sort list elements in ascending order.

Concepts Used:
- Tuple
- List
- Tuple Method: count()
- List Method: sort()
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

grades = ("C", "D", "A", "A", "B", "B", "A")

# Count the occurrence of 'A' in the tuple
print("Grade 'A' appears", grades.count("A"), "times.")

# Create a list of grades
grade = ["C", "D", "A", "A", "B", "B", "A"]

# Sort the list in ascending order
grade.sort()

print("Sorted Grades:", grade)