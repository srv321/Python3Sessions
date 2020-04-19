score = [10, 20, 67, 45, 90]
print(score)  # [10, 20, 67, 45, 90]

print(score[0])  # 10
print(score[4])  # 90
print(score[-1])  # 90
print(score[-5])  # 10
# 0-4 slicing
#   -1-2-3-4-5

print(score[:])  # new/shallow copy of list [10, 20, 67, 45, 90]

print(score + [1, 2, 3])  # [10, 20, 67, 45, 90, 1, 2, 3]
print(score + ["A", "B", "C"])  # [10, 20, 67, 45, 90, 'A', 'B', 'C']

number = [1, 2, 3, 4, 5]
number[2] = 90  # [1, 2, 90, 4, 5]
print(number)

# append:
number.append(100)
print(number)  # [1, 2, 90, 4, 5, 100]

number.append(7 ** 3)
print(number)  # [1, 2, 90, 4, 5, 100, 343]

name = ['a', 'b', 'c', 'd', 'e', 'f']
print(name)  # ['a', 'b', 'c', 'd', 'e', 'f']
name[2:5] = ['C', 'D', 'E']
print(name)  # ['a', 'b', 'C', 'D', 'E', 'f']
name[2:5] = []
print(name)  # ['a', 'b', 'f']

name[:] = []
print(name)  # []
name.append([1, 2, 3])
print(name)  # [[1, 2, 3]]

test = [20, 30, 40, 50, 60]
print(len(test))  # 5

# nested lists:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  # ['a', 'b', 'c']
print(x[1])  # [1, 2, 3]

print(x[0][1])  # b
print(x[1][2])  # 3
