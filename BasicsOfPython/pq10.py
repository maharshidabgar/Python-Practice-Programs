"""
===========================================================
🐍 Python Practice Question #10

Question:
Write a Python program to check whether a list is a
palindrome or not.

Objective:
- Learn how to copy a list.
- Reverse a list using the reverse() method.
- Compare two lists to determine whether they are
  palindromes.

Concepts Used:
- List
- copy()
- reverse()
- if-else
- Comparison Operator (==)
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

list1 = ["m", "a", "o", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome...")
else:
    print("Not Palindrome...")