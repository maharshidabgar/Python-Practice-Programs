'''Create a Rectangle class with length and width. 
Create a method area() to calculate the area.'''

class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        area_of_rectangle = self.length * self.width
        print("Area is : ", area_of_rectangle)
len = Rectangle(4, 8)

len.area()