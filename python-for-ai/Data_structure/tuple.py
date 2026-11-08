#creating a tuple
empty=()
points=(3,7)
colors=("red","green","blue")
single=(5,)
without_parenthesis=1,2,3,4,5

#ACCESSING TUPLE ELEMENTS
print(points[0])
print(colors[2])
print(single[0])
print(without_parenthesis[4])

#tuple unpacking
point=(2,3)
x,y=point
print(x)
print(y)
#swap values using tuple unpacking
x,y= y,x
print(x)
print(y)