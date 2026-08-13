'''Create a Circle class that takes radius. 
Create a method area() to calculate the area.'''

class Circle: # Class Declare

    def __init__(self, radius): # Constructor

        self.radius = radius

    def area(self): # Method with only Self

        area_of_circle = 3.14 * self.radius * self.radius

        print("Area of Circle is : ", area_of_circle)

rad = Circle(4) # Object Declare

rad.area() # Main Print object with Method