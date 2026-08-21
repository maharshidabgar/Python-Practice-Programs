class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # Private data


    def reset_var(self):

        print(s1.__marks)

s1 = Student("Maharshi", 85)

print(s1.name)       # Works
print(s1.reset_var())    # Its Run 
