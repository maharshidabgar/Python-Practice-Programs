# single - inheritence

class Car:

    color = "red"
    @staticmethod
    def start():

        print("Car Started...")

    @staticmethod
    def stop():

        print("Car Stopped...")

class ToyotaCar(Car): # Inheritence

    def __init__(self, name):

        self.name = name

car1 =  ToyotaCar("Alto")

car2 =  ToyotaCar("Fortuner")

print(car2.color)

print(car2.start())