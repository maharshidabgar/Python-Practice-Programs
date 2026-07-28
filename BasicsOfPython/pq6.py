"""
===========================================================
🐍 Python Practice Question #06

Question:
Write a Python program to input a number from the user and
check whether it is Even or Odd.

Objective:
- Learn how to use conditional statements.
- Understand the modulus (%) operator.
- Determine whether a number is even or odd.

Logic:
- If the remainder when dividing the number by 2 is 0,
  the number is Even.
- Otherwise, the number is Odd.

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

if num % 2 == 0:
    print("The Number is Even...")
else:
    print("The Number is Odd !")