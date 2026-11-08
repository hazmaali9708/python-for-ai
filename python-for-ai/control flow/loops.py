for i in range(8):
    print(i)

for i in range(1, 11, 2):
    print(i) 

for i in range(10, 0, -1):
    print(i)  

for i in range(5):
    print("Hello World!")     

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

name=input("Enter a letter: ")
for i in name:
    print(i)
#Loop through a list (preview)
name=["apple", "banana", "cherry"]
for i in name:
    print(f"{i} is a fruit")

names=["John", "Jane", "Doe","ali","ahmed"]
for i in names:
    print(f"{i} is a name")

#while loop
counter=0
while counter<5:
    print(f"Counter is at: {counter}")
    counter+=1    