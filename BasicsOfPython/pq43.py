'''Define a Employee class with attributes role, department & 
salary. This class also has a a showDetails() method...'''

class emp:

    def __init__(self, role, dept, salary):

        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):

        print("Role = ", self.role)
        print("Department = ", self.dept) 
        print("Salary = ", self.salary)


'''Create an Engineer class that inherits properties from Employee
& has additional attributes : name & age.'''

class Engineer(emp):

    def __init__(self, name, age):

        self.name = name
        self.age = age
        super().__init__("HR-Manager", "IT", 55000)



en = Engineer("Maharshi", 21)

en.showDetails()

print(en.role)
print(en.age)
print(en.name)
print(en.dept)
print(en.salary)