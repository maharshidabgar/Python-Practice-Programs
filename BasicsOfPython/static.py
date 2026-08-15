# They work on Class level not Use Object

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    @staticmethod # Decorator = use for Without self Parameter usage
    def hello():

        print("Jay SwamiNarayan !")

s1 = Student("Chirag", 25)

s1.hello()