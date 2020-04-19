class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):

    def isEmployee(self):
        return True


# Test Person
emp = Person("Naveen")
print(emp.name) # Naveen
print(emp.getName(), emp.isEmployee()) # Naveen False

emp1 = Employee("Tom")
print(emp1.name) # Tom
print(emp1.getName()) # Tom
print(emp1.isEmployee()) # True
