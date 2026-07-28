"""
===========================================================
🐍 Python Practice Question #08

Question:
Write a Python program to input a number from the user and
check whether it is a multiple of 7 or not.

Objective:
- Learn how to use the modulus (%) operator.
- Practice conditional statements.
- Determine whether a number is divisible by 7.

Logic:
- If the remainder when dividing the number by 7 is 0,
  the number is a multiple of 7.
- Otherwise, it is not a multiple of 7.

Concepts Used:
- input()
- int()
- Modulus Operator (%)
- if-else
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

num = int(input("Enter a Number : "))

if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a Multiple of 7")