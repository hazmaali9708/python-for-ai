my_dict={}
#creating a dictionary
person={
    "name": "john",
    "class": "10th",
    "age": 15,
    "subjects": ["math", "science", "english"]
}
#acccessing values from the dictionary
print(person["name"])
print(person["class"])
print(person["age"])
print(person["subjects"])
print(person.get("name"))
print(person.get("class"))
print(person.get("age"))
print(person.get("subjects"))

#changing values in the dictionary
person["age"]=17
person["subjects"].append("history")
person["email"]="john@example.com"
print(person)
del person["age"]
age=person.pop("age",None)
print(person)

#Dictionary methods
print(len(person))
print(person.keys())
print(person.values())
print(person.items())

if "name" in person:
    print("fonund name in the dictionary")
else:
    print("name not found in the dictionary")    

person.update({"age": 18, "gender": "male"}) 
print(person)   

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"