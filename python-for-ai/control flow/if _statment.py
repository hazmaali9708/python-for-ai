temperature=int(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It is hot outside.")
elif temperature < 10:
    print("It is cold outside.")
elif temperature >=10 and temperature  <= 30:
    print("The weather is moderate.")
else:
    print("Invalid temperature input.")


score=int(input("Enter your score: "))
if score >= 90:
    print("You got an A grade.")
elif score >= 80:
    print("You got a B grade.")
elif score >=70:
    print("You got a C grade.")
elif score >= 60:
    print("You got a D grade.")
elif score < 60 and score >= 50:
    print("You got an E grade.")
elif score < 50:
    print("You got an F grade.")
else:
    print("Invalid score input.")    

#Multiple conditions
age=int(input("Enter your age: "))
if age>=18 and age<=65:
    print("You are eligible to work.")
elif age<18 or age>65:
    print("You are not eligible to work.")    
else:
    print("Invalid age input.")
#Nested if statements

has_ticket= True
age=int(input("Enter your age: "))
if has_ticket:
    if age>=18:
        print("You can enter the concert.")
    else:
        print("need adult supervision.")        
    