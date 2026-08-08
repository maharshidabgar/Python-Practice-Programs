class student:

    # Global Variable Declaration in Class
    
    college_name = "B.N Patel Science College" 

    # Default Constructor

    def __init__(self):

        pass


    # Parameterized Constructors

    def __init__(self, name, marks):

        self.name = name

        self.marks = marks

        print("Adding new Student in Database...")

s1 = student("Param", 89)
print(s1.name, s1.marks) # Param name 

s2 = student("Jenny", 75)
print(s2.name, s2.marks) # Jenny

print(s2.college_name)