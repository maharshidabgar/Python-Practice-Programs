class Stiu: # Class Declaration

    college_name = "B.N Patel Science" # Global Attribute

    def __init__(self, name, marks): # Constructor

        self.name = name
        self.marks = marks

    def welcome(self): # METHOD with Compulsary with Self parameter

        print("Jay Mataji", self.name)

s1 = Stiu("Raman", 57)

s1.welcome()
