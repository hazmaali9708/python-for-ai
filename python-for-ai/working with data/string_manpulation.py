first_name="John"
last_name="Doe"
#concatenation of strings
full_name=first_name+" "+last_name
print(full_name)

#Repitation of strings
star="*"
stars=star*10
print(stars)

name="Fatima"
names=(name*10)
print(names)
#Changing case
test="Hamza Ali Malik"
print(test.lower())
print(test.upper())
print(test.title())

#Cleaning strings
messy="hello word"
print(messy.strip())

price="$19.99"
print(price.strip("$"))

#Finding and replacing strings
text="I like python programming"
print(text.find("python"))
print("python" in text)
print(text.startswith("I"))
print(text.endswith("programming"))
print(text.split(" "))
print(text.count("python"))

new_text=text.replace("python","java")
print(new_text)
