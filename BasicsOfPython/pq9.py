"""
===========================================================
🐍 Python Practice Question #09

Question:
Write a Python program to ask the user to enter the names of
their three favourite movies and store them in a list.
Finally, display the complete list of favourite movies.

Objective:
- Learn how to take multiple user inputs.
- Store multiple values in a list.
- Display list elements using the print() function.

Concepts Used:
- input()
- List
- Variables
- print()

Author : Maharshi Dabgar
Language : Python 3
Repository : Python-Practice-Programs

===========================================================
"""

movi1 = input("Enter your 1st Fav Movie : ")
movi2 = input("Enter your 2nd Fav Movie : ")
movi3 = input("Enter your 3rd Fav Movie : ")

listofMovie = [movi1, movi2, movi3]

print("Your Favourite 3 Movies List:\n", listofMovie)