class Base1(object):
    def __init__(self):
        self.str1 = "Naveen"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Tom"
        print("Base2")


class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child")

    def printStrings(self):
        print(self.str1, self.str2)


ob = Child()  # Base1,Base2,Child
ob.printStrings()  # Naveen Tom
