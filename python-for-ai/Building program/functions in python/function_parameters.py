#without parameter
def greet():
    print("hello alice")
greet()
#with parameters

def greet(first_name,last_name):
    print(f"hello {first_name} {last_name}")
greet("Malik","Hamza") 


def introduce(name,age):
    print(f"My name is {name}")
    print(f"My age is {age}")
introduce("ali",20) 

def cal_tax(price,tax_rate,amount):
    tax=price*tax_rate
    final= price+tax-amount
    print(final)

cal_tax(100,0.1,0.2)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
greet("Alice")           # Hello, Alice!

# Override default
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)
