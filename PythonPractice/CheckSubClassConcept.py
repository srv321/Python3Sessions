class Base(object):
    pass  # Empty Class


class Child(Base):
    pass  # Empty Class


# Test Code:
print(issubclass(Child, Base))  # True
print(issubclass(Base, Child))  # False

c = Child()
b = Base()

print(isinstance(b, Child))  # False
print(isinstance(c, Child))  # True
print(isinstance(c, Base))  # True
