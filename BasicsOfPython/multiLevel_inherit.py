# Multi - Level Inheritence

class Car: # Level 1

    @staticmethod
    def start():

        print("Car started...")

    @staticmethod
    def stop():

        print("Car stopped...")

class ToyotaCar(Car): # Level 2

    def __init__(self, brand):

        self.brand = brand

class Fortuner(ToyotaCar): # Level 3

    def __init__(self, type):

        self.type = type

car1 = Fortuner("Diesel")

car1.start()
