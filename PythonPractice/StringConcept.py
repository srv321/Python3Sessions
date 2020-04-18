s1 = "test selenium"
s2 = 'hello world'

print(s1)
print(s2)

print(s1[0])
# print(s1[13]) string index out of range

print(s1 + " " + s2)

print("hello \n world")
print("hello \t world")

print("test" * 5)

print(s1[0:5])

print("test" in s1)
print("java" not in s1)

print("my name is %s and my age is %d" % ("Tom", 25))  # formatting operator

s3 = '''test java
test python
test selenium
and 
this is my python code'''

print(s3)

s4 = """"hi this is my python code
and im learning python
and im so happy"""

print(s4)

print('hi i\'m saurav')
print("hi my fav language is \"python\" and im so happy")

str = "this is my Python Code and I love Python z"
print(str)
print(str.capitalize())  # This is my python code and i love python z

print(str.count("Python"))  # 2
print(str.count("Code"))  # 1

print(str.find("Saurav"))  # -1

print(len(str))
print(str.lower())  # this is my python code and i love python z

str1 = " hello "
print(str1.lstrip())  # hello
print(str1.rstrip())  # hello

print(max(str))  # z
str2 = "abz"  # a
print(min(str2))

str3 = "Hello Test Python"
print(str3.replace("Hello", "Bye"))  # Bye Test Python

str4 = "java hello python hello javascript"
str5 = str4.split("hello")
print(str5)  # ['java ', ' python ', ' javascript']
print(str5[0])  # java

print(str4.upper())  # JAVA HELLO PYTHON HELLO JAVASCRIPT

st = "Python"
print(st[5])  # n
print(st[-1])  # n
print(st[-6])  # P
print(st[0])  # P

a = "test gjggj jgj gjjjg"
b = "test gjggj jgj gjjjg"
print(a is b)  # True

p = "test!"
q = "test!"
print(p == q)

h = "India !"
g = "India !"
print(h == g)
