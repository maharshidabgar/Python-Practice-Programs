'''Create a Person class with name and age. Create a method introduce() that prints:
My name is Maharshi and I am 21 years old.'''

class person(): 

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def introduce(self):

        print("My name is", self.name, "and I am", self.age, "years old.")

per = person("Tanmay", 45)

per.introduce()