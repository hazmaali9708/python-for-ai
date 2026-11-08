#syntax of function

def greet():
    print("Hello")
greet()    

#function with logix
def check_weather():
    temp=40
    if temp < 20:
        print("It is cold")
    else:
        print("it is hot")
check_weather() 




def check_weather():
    temperature=30
    if temperature<= 20:
        print("It is cold")
    else:
        print("It is hot")

check_weather()  

#global variables
discount_rate=0.15
def apply_discount(price):
    prices=price*discount_rate
    return price-prices
result=apply_discount(200)
print(result)
#practice question
tax=0.1
def calculate_tax(amount):
    amounts=amount*tax
    return amount+amounts
results=calculate_tax(100)
print(results)




 




