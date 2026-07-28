"""
===========================================================
🐍 Python Practice Question #04

Question:
Write a Python program to input two integers from the user
and check whether the first number is greater than or equal
to the second number.

Objective:
- Learn how to compare two numbers.
- Understand relational operators.
- Use conditional statements to display the result.

Concepts Used:
- input()
- int()
- Relational Operator (>=)
- if-else
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

a = int(input("Enter a Num : "))
b = int(input("Enter b Num : "))

if a >= b:
    print("True")
else:
    print("False")