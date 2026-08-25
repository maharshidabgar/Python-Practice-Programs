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


sd = emp("HR-Manager", "IT", 55000)

sd.showDetails()