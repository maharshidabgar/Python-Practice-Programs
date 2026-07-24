# List Declaration

marks = [12.5, 98.9, 87.5, 95.2, 66.4, 45.3]

print(marks)

print(type(marks))

print(marks[0]) # printing the 0 index marks in List

print(marks[2])

print(len(marks)) # Length of List

marks[1] = 96.5 # Changes 1 indexed 98.9 to 96.5 permenantly in List

print(marks)

student = ["Maharshi", 392, 7.89, "Anand"]

print(student[0])

student[0] = "Nidhi" # List is Mutable in Python also Access 

print(student) # String is Immutable means only Access not Change

print(student[5]) # Throws Error bcz 5 index not exist in this List

