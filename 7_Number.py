# Python Numbers :-

#* There are three numeric types in Python:
# 1. int
# 2. float
# 3. complex

# examples :-------
# variable declaration:
num = 89
print(num)

fnum = 90.9
print(fnum)

cnum = 1j
print(cnum)

#* to verify the type of any object in Python, use the "type()" function:-----
print(type(num)) 
print(type(fnum)) 
print(type(cnum)) 

#* type conversion:----- 
#? python me, constructor function bhi hote hain jaise `int()`, `float()`, `complex()`, etc ye sabhi constructor functions hain. jo ki type conversion me help karte hain.
# variable declaration by using
count = int(87.9)
print(count)
print(type(count))

age = float(31)
print(age)
print(type(age))

math = complex(89)
print(math)
print(type(math))

#* generate random number :- 
import random

rndnum = random.randrange(1, 10)
print(rndnum)