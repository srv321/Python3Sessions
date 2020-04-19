# set - not order based
# it stores different types of data
# it performs different mathematical operations
# it doesnot store duplicate elements

# define a set: use {}

s1 = {100, "Tom", 12.33, True, "Tom"}
s2 = {1, 2, 1, 2, 1, 1, 3, 2}
print(s2)  # {1, 2, 3}
print(s1)  # {12.33, True, 100, 'Tom'}

# set() function:

s3 = set("python")
print(s3)  # {'h', 't', 'o', 'y', 'p', 'n'}

s4 = set([30, 40, 20, 34, 20])
print(s4)  # {40, 34, 20, 30}

s5 = set((10, 20, 45, 43))
print(s5)  # {10, 43, 20, 45}

# while creating a set object, you can store only Numbers.String,tuple
# list and dictionary objects are not allowed, list is allowed with set function
# only immutable objects are allowed with set object like tuple

set1 = {(10, 20), 30, 40}
print(set1)  # {40, (10, 20), 30}

# set2 = {[10,20],30,40}
# print(set2) # unhashable type: 'list'

# set Operations:
# union: |
p1 = {1, 2, 3, 4, 5}
p2 = {4, 5, 6, 7, 8}
print(p1 | p2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(p1.union(p2))  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: &
p3 = {1, 2, 3, 4, 5}
p4 = {4, 5, 6, 7, 8}
print(p3 & p4)  # {4, 5}
print(p3.intersection(p4))  # {4, 5}

# difference of sets:- or difference()
p5 = {1, 2, 3, 4, 5}
p6 = {4, 5, 6, 7, 8}
print(p5 - p6)  # {1, 2, 3}
print(p6 - p5)  # {8, 6, 7}
print(p5.difference(p6))  # {1, 2, 3}
print(p6.difference(p5))  # {8, 6, 7

# symmetric difference : ^
p7 = {1, 2, 3, 4, 5}
p8 = {4, 5, 6, 7, 8}
print(p7 ^ p8)  # {1, 2, 3, 6, 7, 8}
print(p7.symmetric_difference(p8))  # {1, 2, 3, 6, 7, 8}

# Set - In Built methods:
# 1. add():
s1 = {"Java", "Python", "C++"}
s1.add("Perl")
print(s1)  # {'Perl', 'Java', 'Python', 'C++'}

# 2. update():
s2 = {"Java", "Python", "C++"}
s2.update(["C", "VBA"])
print(s2)  # {'C', 'Java', 'C++', 'Python', 'VBA'}

s2.update(("Ruby", "JavaScript"))
print(s2)  # {'JavaScript', 'C', 'C++', 'Ruby', 'Python', 'VBA', 'Java'}

# 3. clear():
s2.clear()
print(s2)  # set()

# 4. copy():
lang = {"Java", "Python", "C++"}
lang1 = lang.copy()
print(lang1)  # {'Python', 'Java', 'C++'}

# 5. discard():
lang = {"Java", "Python", "C++"}
lang.discard("C++")
print(lang)  # {'Python', 'Java'}
lang.discard("Naveen")  # discard gives no error even if value doesnt exist
print(lang)  # {'Python', 'Java'}

# 6. remove():
student = {"Naveen", "Tom", "Steve", "Peter"}
student.remove("Tom")
print(student)  # {'Steve', 'Naveen', 'Peter'}

# student.remove("Simon")
# print(student)  # KeyError: 'Simon'-> remove gives error if value doesnt exist
