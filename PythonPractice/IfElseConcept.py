x = int(input("please enter the value of x"))  # just like scanf function in java

if x < 0:
    print("x is a negative number")
elif x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is equal to zero")
else:
    print("not defined")

if True:
    print("PASS")
else:  # dead code
    print("FAIL")

if 10 > 5:
    print("Hi")

# WAP to find out the highest number

a = 500
b = 600
c = 800

if a > b and a > c:
    print("a is the highest number")
elif b > c:
    print("b is the highest number")
else:
    print("c is the highest number")

total = int(input("enter the total value"))
if total < 100:
    total = total + 20
elif total >= 100 and total <= 500:
    total = total + 50
else:
    total = total + 100

print(total)  # no concat 800
print("total=" + str(total))  # str method total=800
print(f'{"total value="}{total}')  # f strings total value=800
