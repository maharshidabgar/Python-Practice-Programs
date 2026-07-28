"""
===========================================================
🐍 Python Practice Question #05

Question:
Write a Python program to:
1. Input the user's first name and display its length.
2. Count the number of occurrences of the '$' symbol in a
   given string.

Objective:
- Learn how to work with strings.
- Find the length of a string.
- Count the occurrences of a specific character in a string.

Concepts Used:
- input()
- len()
- String Method: count()
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

fname = input("Enter Your First Name : ")

print("Length of your name is", len(fname))

text = "Avo avo MAma $500 lavela and me $600 pacha apya $100 dollar vadharya..."

print("In this string '$' sign occurs", text.count("$"), "times.")