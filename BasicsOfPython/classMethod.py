class Person:

    name = "anonymous"

    @classmethod # change the name is class using cls keyword

    def changeName(cls, name):

        cls.name = name


p1 = Person()
p1.changeName("Rahul Modi")
print(p1.name)
print(Person.name)