def test():
    print("Hello World")


test()


def abc(a):
    print(a + 10)


abc(10)


# optional/default parameter:

def getCountryName(name="India"):
    print(name)


getCountryName()
getCountryName("UK")
getCountryName(100)


# pass a list to a function:
def getNames(list):
    for x in list:
        print(x)


names = ["Java", "Python", "DoTNET", "Ruby"]
getNames(names)


# function with return:
def sum(a, b):
    c = a + b
    return c


s1 = sum(10, 20)
print(s1)


def getCapitalName(countryName):
    if countryName == "India":
        return "New Delhi"
    elif countryName == "USA":
        return "Washington DC"


print(getCapitalName("India"))
print(getCapitalName("USA"))


def launchBrowser(browserName):
    if browserName == "chrome":
        print("launch google chrome")
    elif browserName == "firefox":
        print("launch firefox")
    else:
        print("no browser is defined")


launchBrowser("chrome")


# Recursion in Python: a func is calling itself
# WAP to get the factorial of a given number:
# fact(4) = 4*3*2*1=24
# fact(5) = 5*4*3*2*1=120

def fact(num):
    if num > 1:
        num = num * fact(num - 1)
    return num


print(fact(4))
print(fact(5))


def login(username, password):
    print("login with %s and %s" % (username, password))


login("Saurav@gmail.com", "test@123")
