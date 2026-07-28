'''WAP to enter marks of 3 subjects from the user & store them in
a dictionary. Start with an empty dict & Add one by one. 
Use subject name as Key & marks as Values...'''

marks = {} # Empty Dict

mark1 = int(input("Enter Phy Marks : "))
marks.update({"Phy": mark1})

mark2 = int(input("Enter Math Marks : "))
marks.update({"Math": mark2})

mark3 = int(input("Enter Chem Marks : "))
marks.update({"Chem": mark3})

print(marks) 