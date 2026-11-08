my_list=["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple
print(my_list[1])  # Output: banana
print(my_list[2])  # Output: cherry
my_list.append("orange")
print(my_list)
my_list.remove("apple")  # Output: ['banana', 'cherry', 'orange']
print(my_list)
my_list.insert(1, "kiwi")
my_list.sort()
print(my_list)  # Output: ['banana', 'cherry', 'kiwi',
my_list.reverse()
print(my_list)  # Output: ['kiwi', 'cherry', 'banana']
list=input("Enter a list of items separated by commas: ")
print(list.split(","))  # Output: ['item1', 'item2', 'item3'] (example output based on user input)

lists=["apple", "banana", "cherry"]
print(lists[0:3])
print(lists[:-2])

#list method
let=[1,2,7,2,1,3,4,5,8,9,10]
print(len(let))  # Output: 5
print(let.count(2))  # Output: 1
print(let.index(4))  # Output: 
let.sort()  # Output: [1, 2, 3, 4, 5, 8, 9, 10]
print(let)

new_let=let.copy()  # Output: [1, 2, 3, 4, 5, 8, 9, 10]
print(new_let)

fruit=["apple", "banana", "cherry"]
if "apple" in fruit:
    print("Yes, apple is in the list")
else:
    print("No, apple is not in the list")

if fruit:
    print("The list is not empty")
else:
    print("The list is empty")            