#Local variables
#Variables created inside a function only exist within that function:
def price():
    pr=100
    tax=pr*0.1
    print(f"total:{tax+pr}")
price()    

#Global variables
#Variables created outside functions can be accessed anywhere:

disc=0.15
def discount(price):
    discoun=price*disc
    return price-discoun
result=discount(100)
print(result)

#Modifying global variables
#To change a global variable inside a function, use the global keyword:

counter=4
def increment():
    global counter
    counter+=1
increment()
increment()
print(counter)    

#practice
def add_amount(current_amount,amount):
    return current_amount + amount
res=add_amount(200,200)
print(res)


