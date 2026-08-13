'''Create an Employee class that takes name and salary. 
Create a method display_salary() to print the salary.'''

class Emp:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display_salary(self):

        print("Employee name is", self.name, "& his/him salary is", self.salary, "!")

eo = Emp("Manish", 75000)

eo.display_salary()

