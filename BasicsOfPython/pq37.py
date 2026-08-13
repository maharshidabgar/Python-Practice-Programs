'''Create a Calculator class with two numbers and methods:

add()
subtract()
multiply()'''

class Calculator:

    def __init__(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

    def add(self):

        print("Sum is : ", self.num1 + self.num2)

    def subtract(self):

        print("Sub is", self.num1 - self.num2)

    def multiply(self):

        print("Mul is : ", self.num1 * self.num2) 

cal = Calculator(15, 5)

cal.add()
cal.subtract()
cal.multiply()



        