# Tuple : is a collection of elements of any python data type
# Tuple vs List:
# 1. syntax: you have to store the values in a tuple with (), but in List:[]
# 2. Tuple is immutable but List is mutable

marks = (100, 20, 30, 400)
employeeData = ("Tom", 25, 'm', 23.33, True)

print(employeeData)  # ('Tom', 25, 'm', 23.33, True)

print(employeeData[0])  # Tom
print(employeeData[3])  # 23.33

# print(employeeData[5]) # tuple index out of range

print(employeeData[-1])  # True
print(employeeData[-5])  # Tom

list = [10, 20, 30, 40]  # mutable- can be changed
list[1] = 100
print(list)  # [10, 100, 30, 40]

# immutable - can not change the elements
# names = ("Java","Dot Net","Python","C Sharp")
# names[2]="English"
# print(names) # TypeError:Tuples don't support item assignment

# names = ("Java","Dot Net","Python","C Sharp")
# del names
# print(names)

# concatenation of tuples
t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 + t2)  # (1, 2, 3, 1, 2, 3)

t3 = (1, 2, 3)
print(t3 * 4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

# Range Slice:
t4 = (1, 2, 3, 4, 5, 6)
print(t4[1:3])  # (2, 3)

# in
employeeData1 = ("Tom", 25, 'm', 23.33, True)
print(25 in employeeData1)  # True
print(35 in employeeData1)  # False

# not in:
print(35 not in employeeData1)  # True

# len:
length = len(employeeData1)
print(length)  # 5

# max number:
number = (12, 11, 30, 20, 40)
print(max(number))  # 40

names1 = ("Java", "Dot Net", "Python", "C Sharp")
print(max(names1))  # Python

alpha = ("abc", "cde", "efg")
print(max(alpha))  # efg
print(min(alpha))  # abc
