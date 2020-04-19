name = "Alexander"
for i in name:
    print(i)
    if i == 'x':
        break

print("---------")

name = "Alexander"
for i in name:
    print(i)
    if i == 'x':
        continue

str = ["python", "java", "C Sharp", "Dot Net"]
for l in range(len(str)):
    print(str[l])
    if (str[l] == "java"):
        print("hey I found Java!!!")
        break

print("---------")

lang = ["Hindi", "English", "Spanish", "German", "Chinese"]
flag = False
for index in range(len(lang)):
    print(lang[index])
    if (lang[index] == "Spanish"):
        print("Spanish is the 2nd popular language in the world")
        flag = True
        break
if (flag):
    print("I want to learn Spanish")
