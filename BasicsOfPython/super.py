# super() method use for Parent class attribute using in Child class

class Car:

    def __init__(self, type):

        self.type = type

    @staticmethod
    def start():

        print("Car Started !")

    @staticmethod
    def stop():

        print("Car Stopped !")

class ToyotaCar(Car):

    def __init__(self, name, type): # type parent class Attribute also declare

        self.name = name
        super().__init__(type) # Super Method Usage

car1 = ToyotaCar("Prius", "Electiric")
print(car1.type)