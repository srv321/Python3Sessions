class Employee:
    # hidden data member or private member of Employee class
    __salary = 1000


e1 = Employee()
# print(e1.__salary) --this is not the right way of accessing hidden private variable

# access private hidden variable by using tricky syntax:
print(e1._Employee__salary)
