'''WAP to enter marks of 3 subjects from the user & store them in
a dictionary. Start with an empty dict & Add one by one. 
Use subject name as Key & marks as Values...'''

marks = {} # Empty Dict

sub1 = input("Enter Sub1 Name : ")
marks[sub1] = int(input("Enter Marks : "))

sub2 = input("Enter Sub2 Name : ")
marks[sub2] = int(input("Enter Marks : "))

sub3 = input("Enter Sub3 Name : ")
marks[sub3] = int(input("Enter Marks : "))

print(marks)