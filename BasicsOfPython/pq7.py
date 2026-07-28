"""
===========================================================
🐍 Python Practice Question #07

Question:
Write a Python program to input three numbers from the user
and find the greatest (largest) among them.

Objective:
- Learn how to compare multiple values.
- Practice logical operators with conditional statements.
- Identify the largest number among three inputs.

Concepts Used:
- input()
- int()
- if-elif-else
- Logical Operator (and)
- Relational Operator (>=)
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

num1 = int(input("Enter 1st Num : "))
num2 = int(input("Enter 2nd Num : "))
num3 = int(input("Enter 3rd Num : "))

if num1 >= num2 and num1 >= num3:
    print("Greatest Number is", num1)

elif num2 >= num1 and num2 >= num3:
    print("Greatest Number is", num2)

else:
    print("Greatest Number is", num3)