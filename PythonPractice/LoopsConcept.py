# while loop:

count = 0
while count < 10:
    print("Hello World")
    print(count)
    count = count + 1

print("---------")

num = 0
while num < 3:
    print("Hello Python")
    num = num + 1
else:
    print("Bye Python")

print("---------")

# for loop:
name = ["java", "python", "dot net", "c sharp"]
for i in name:
    print(i)

print("---------")

str = "I love python"
for i in str:
    print(i)

print("---------")

list = ["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])

print("---------")

# for loop with else
CountryList = ["India", "USA", "UK", "Germany"]
for index in range(len(CountryList)):
    print(CountryList[index])
else:
    print("CountryList is over")

print("---------")

CityList = ["Kolkata", "NY", "LA", "Berlin"]
for index in range(2):
    print(CityList[index])
else:
    print("CityList is over")

print("---------")

# nested for loop:
for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()
