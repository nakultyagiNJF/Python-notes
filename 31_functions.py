# !Functions:-
# *A function is a block of code which only runs when it is called.
# *We can pass data, know as parameters into a function.
# *A function can return data as a result.

# examples:--

# ? Define Simple Function:-
# 1.
# create function:
def any_func():
    print("Hi Shree!!")
    
# calling a function:
any_func()
any_func()

# NOTE: basically functions ko ham isliye banate hain kyonki same code ko reuse kar paye... or multiline code ko function ke category me daal kar us function ko jitni baar chahe utni baar call kar sakte ho jisse ki code complexity bhi kam hoti hai.


# ?Arguments and Parameters:-
# *The terms 'parameter' and 'argument' can be used for the same thing: information that are passed into a function.
# --- Parameter:--- A parameter is the variable listed inside the parentheses in the function definition.
# --- Argument:--- An argument is the value that is sent to the function when it is called.

# 2.
def info(name, age, city):
    print(f"My name is {name}. I am {age} years old. I am living in {city}.")
    
info("Ayushi Sharma", 29, "Gurugram")
info("Tushar Sharma", 25, "New Delhi")

# 3.
def sum(a, b, c):
    print("sum is : ", a + b + c)

sum(10, 6, 45)
sum(90, 8, 12)

# ?Arbitary Arguments, '*args'
# 4.
def nums(a, *b):
    print(a)
    print(b)
    print(type(b))

nums(1, 2, 3, 4, 5, 6, 7, 8)
 
# ?Default Parameters:-
# 5. 
def default(name, city="Noida"):
    print(name)
    print(city)
    
default("Mohan", "New Delhi")

# ?Keyword Arguments:-
# *we can also send arg with the key=value syantax.
# 6.
def details(name, age, city):
    print(f"name is {name}. age is {age}. city is {city}.")
    
details(city="Noida", name="Ayushi Jain", age=28)

# ?Pass any data type as an argument:-
def names(name):
    for n in name:
        print(n)
    
any_names = ['mohan', 'sohan', 'sohan', 'anuj', 'gopal']
names(any_names)

# ?Arbitrary Keyword Arguments, **kwargs:---------------------
# 8.
def my_info(**kid):
    print(f"My name is {kid["fname"]} {kid["lname"]}. I am {kid["age"]} years old. i am very my much {kid["Feeling"]}. i want to go {kid["destination"]}")


my_info(fname="Ayushi", lname="Joshi", age=24, Feeling="sad", destination="home")

# you can use multiple variable in the **kwargs parameter

# ?Return Values:--------------------------
# 9.
def addition(a, b):
    return a + b

res = addition(10, 60)
print(res)

# 10.
def myInfo(name, age, city):
    return f'my name is {name}. i am {age} years old. i am living in {city}.'
    
data = myInfo('mohan kumar', 45, 'new delhi')
print(data)

# ?The "pass" statement:------------
# *Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# 11.
def pasing():
    pass
    
pasing()

# ?Recursion:-----------------------
# *Python also accepts function recursion, which means a defined function can call itself.
# 12.
def recur(num):
    if (num > 0):
        res = num + recur(num - 1)
    else:
        return 0
    
    return res

output = recur(5)
print(output)

# 5 + 4 + 3 + 2 + 1

#! Python Lambda Function:-

#* A lambda function is a small anonymous function.
#* A lambda function can take any number of arguments, but can only have one expression. 
#* Syntax:- lambda arguments : expression

# examples:
# 1.
sum = lambda a, b : print(a + b)
sum(4, 5)
'''
    sum --> variable name
    lambda --> keywords
    a, b --> parameters
    : --> colon for block
    print(a + b) --> expression
    sum(4, 5) --> function call with arguments
'''

# 2.
sayHi = lambda name : print("Hello " + name)
sayHi("Gopal Bhardwaj")

# 3. with return function:
info = lambda name, age, city : f"My name is {name}. I am {age} years old. I am living in {city}."
print(info("Gopal Bhardwaj", 28, "San Francisco"))

# 4. parameters with input:

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

info = lambda name, age, city : f"My name is {name}. I am {age} years old. I am living in {city}."
print(info(name, age, city))

#* return function in a function:
def main():
    return lambda a, b : a * b

out = main()
print(out(2, 3)) 