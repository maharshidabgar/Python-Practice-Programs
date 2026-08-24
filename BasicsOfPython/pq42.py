'''Define a Circle class to create a circle with radius r using the Constructor.
Define an Area() method of the class which calculates the area of the circle.
Define a Parameter() method of the class which allows you to calculate the perimeter of the 
circle...'''

class Circle:

    def __init__(self, rad):

        self.rad = rad

    def area(self):

        return 3.14 * self.rad * self.rad

    def parameter(self):

        return 2 * 3.14 * self.rad

cir = Circle(4)

print("Area = ", cir.area())

print("Perimiter = ", cir.parameter())

    


    
