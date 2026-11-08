#creating set
import string


import string


empty_set=set()
numbers={1,2,3,4,5,6,7,8,9,10}
numbers_with_duplicates=set([1,2,3,4,5,6,7,8,9,10,1,2,3])
#accessing set elements 
print(numbers)
print(numbers_with_duplicates)

#BASIC OPERATIONS ON SETS
colors={"red","green","blue"}
#adding elements to the set
colors.add("yellow")
print(colors)

colors.update(["orange","purple"])
print(colors)

#removing elements from the set


colors.remove("red")
print(colors)
colors.discard("marganda")
print(colors)

#remove duplicates
set_with_duplicates=set([1,2,3,4,5,6,7,8,9,10,1,2,3])
print(set_with_duplicates)



allowed_colors={"red","green","blue"}
if "red" in allowed_colors:
    print("Color is allowed")
else:
    print("Color is not allowed")    