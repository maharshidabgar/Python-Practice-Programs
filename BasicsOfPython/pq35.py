'''Create student class that takes name & marks of 3 subjects
as arguments in constructor. Then create a method to print the Average.'''

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Average marks:", avg)


s1 = Student("Maharshi", 80, 90, 70)

print("Name:", s1.name)
s1.average()