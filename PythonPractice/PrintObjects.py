# string representation of class object:
#object printing concept:

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # <__main__.Test object at 0x011CC028> if both str and repr mthds are commented out

    def __repr__(self):
        return "x:%s y:%s" % (self.x, self.y)  # x:10 y:20 if str mthd is commented out

    def __str__(self):
        return "value of x is %s and y is %s" % (self.x, self.y)
        # value of x is 10 and y is 20


# Test Code:
t = Test(10, 20)
print(t)
