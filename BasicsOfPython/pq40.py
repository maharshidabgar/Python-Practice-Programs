'''Create a Circle class that takes radius. 
Create a method area() to calculate the area.'''

class Circle:

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        area_of_circle = 3.14 * self.radius * self.radius

        print("Area of Circle is : ", area_of_circle)

rad = Circle(4)

rad.area()