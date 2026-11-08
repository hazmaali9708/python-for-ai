#Functions
#Return values
#Get results back from your functions
def add_res(a,b):
    return a + b
res=add_res(5,3)
print(res)


def calculate_Area(width,height):
    area=height*width
    return area
room_area=calculate_Area(10,14)
print(room_area)


def double(number):
  return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")

