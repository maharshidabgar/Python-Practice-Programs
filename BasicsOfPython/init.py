class student:

    def __init__(self, fullname):

        self.name = fullname

        print("Adding new Student in Database...")

s1 = student("Param")
print(s1.name) # Param name 

s2 = student("Jenny")
print(s2.name) # Jenny