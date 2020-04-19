def login(username, password):
    print(username, password)


login("naveen", "test123")
login(username="naveentest", password="test@123")


# *arg
def getMarks(*arg):
    for x in arg:
        print(x)


getMarks(10, 23, 78, 45, 80)
getMarks("A", "A+", "B", "B-")


# keyword args:
# **arg

def getStudentMarks(**args):
    for key, value in args.items():
        print("%s == %s" % (key, value))


getStudentMarks(naveen=10, tom=20, peter=30)
getStudentMarks(key="apple", sellerName="Xeon")

# Lamda functions: Anonymous function:
# a fun without a name:

cube = lambda x: x * x * x

print(cube(4))

total = lambda marks: marks + 30

print(total(100))
