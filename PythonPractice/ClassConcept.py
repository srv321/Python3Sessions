class Car:
    # class variables
    wheels = 4

    # Constructor of this class:

    def __init(self):  # const overloading not possible in python
        print("default class const")

    def __init__(self, color):
        print("Car class const")
        self.color = color

    def test(self):
        print("test method")

    # if any var declared inside the method or constructor: instance variable
    def setPrice(self, price):
        self.price = price

    def getprice(self):
        return self.price


# how to create an Object of this class:
c1 = Car("Red")
print(c1.wheels)
print(Car.wheels)  # here we can directly call obcts by classname, no static concept like java

c1.test()
c1.setPrice(1000)
print(c1.getprice())

c2 = Car("Black")
c2.setPrice(3000)
print(c2.getprice())


class Test:
    a = 10


# blank class:
class Pop:
    pass


p1 = Pop
