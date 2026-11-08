# Basic math
print(10 + 3)   # 13 - Addition
print(10 - 3)   # 7  - Subtraction
print(10 * 3)   # 30 - Multiplication
print(10 / 3)   # 3.333... - Division (always gives float)

# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)   # 1  - Modulo (remainder)
print(10 ** 3)  # 1000 - Exponent (power)

#comparison operators
age=21
print(age==20)
print(age!=20)
print(age>20)
print(age<20)
print(age>=20)
print(age<=20)

#logical operators
age = 25
has_license = True

# AND - both must be true
can_drive = age >= 18 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

#truth table
print("Truth Table for AND, OR, NOT")
#AND 
print(True and True)
print(True and False)
print(False and True)
print(False and False)
#OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)
#NOT
print(not True)
print(not False)
#ASSIGNMENT shortcuts
# Instead of:
#score = score + 10

# Write:
#score += 10

# Works with all operators
x = 10
x += 5 

x *= 2    # x is now 30
print(x)