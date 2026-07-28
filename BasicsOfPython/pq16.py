"""
===========================================================
🐍 Python Practice Question #13

Question:
Write a Python program to calculate the admission fee based
on the user's age group and gender using conditional
statements.

Fee Criteria:
- Age 1 or 2 and Gender = M → Fee = 100
- Age 3 or 4 and Gender = F → Fee = 200
- Age 5 and Gender = M → Fee = 300
- Otherwise → No Fee

Objective:
- Learn how to use nested logical conditions.
- Practice relational and logical operators.
- Implement decision-making using if-elif-else.

Concepts Used:
- input()
- int()
- if-elif-else
- Logical Operators (and, or)
- Comparison Operator (==)
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

A = int(input("A : "))
G = input("M/F : ")

if (A == 1 or A == 2) and G == "M":
    print("Fee is 100")

elif (A == 3 or A == 4) and G == "F":
    print("Fee is 200")

elif A == 5 and G == "M":
    print("Fee is 300")

else:
    print("No Fee!")