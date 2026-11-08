
import random
#roll a dice
print(random.randint(1, 6))
#Toss 
print(random.choice(["Head","Tail"]))

#pick a random winner
names = ["Ali", "Sara", "Hamza", "Ayesha"]
print(random.choice(names))

#Shuffle a list
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

import string
chars = string.ascii_letters + string.digits
password = "".join(random.choices(chars, k=8))
print(password)

#Random OTP (4 digits)
otp = random.randint(1000, 9999)
print(otp)

#Split data randomly (train/test, useful in ML)

data = list(range(10))
random.shuffle(data)
train = data[:8]
test = data[8:]

#Repeatable results
random.seed(42)
print(random.randint(1, 100))  # same number every run

