class Student:

    def __init__(self, name):

        self.name = name

s1 = Student("Chirag")

del s1.name # del - keyword using for object s1's property delete work

del s1 # direct delete object Through del - keyword

print(s1.name)