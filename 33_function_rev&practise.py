#! Functions :->
#* Python Functions is a block of statements that does a specific task.
#* The idea is to put some commonly or repeateadly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.   

#? Benefits of Using Functions:-
# *Code Reuse
# *Reduced code length
# *Increased readability of code
# *Easier to debug

#? Function Declaration:-
# syntax to declare a function is:
'''
    def function_name(parameters):
        function_body # statement
        return statement
'''   

#? Types of Functions:-
# there are different types of functions:-
#* 1. Built-in Functions
#* 2. User-defined Functions  

#! Creating a Function:-
#* We can define a function in Python, using the `def` keyword. We can add any type of functionalities and properties to it as we require.

#! Calling a Function:-
#* After creating a function in Python we can call it by using the name of the functions Python followed by parenthesis containing parameters of that particular function.

# example:-
# 1.
def myfun():
    print("Hello Shree!")

myfun()

# 2.
def add():
    a = 10
    b = 20
    print(a + b)

add()

#! Parameters or Arguments?

#* Parameters :----> A parameter is the variable listed inside the parentheses inthe function declaration.

#* Arguments :----> An argument is the value that is sent to the function when it is called.

# examples:-
# 1.
def my_info(name, age, city):
    print(f"My name is {name}. I am {age} years old. I am living in {city}.") 
    
my_info("Mohan", 45, "New Delhi")

# re-use the `my_info` function with new inputs:
my_info("Ayushi", 24, "Agra")
my_info("Tushar", 34, "Mathura")

#! Arbitary Arguments, *args:---->

#* If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

#* This way the function will receive a `tuple` of arguments, and can access the items accordingly:  

# examples:
# 1.
def my_data(*names):
    # create a loop for iterate all names:
    for name in names:
        print(name)

my_data('mohan', 'sohan', 'anuj', 'gopal', 'tushar', 'ayushi', 'anupam', 'anuradha', 'madhavi')


#! Keyword Arguments:----->
#* you can also send arguments with the key=value syntax.
#* This way the order of the arguments will not matter, and you will be able to call the function with the arguments in any order you like:

# example:
# 1.
def my_info(name, age, city):
    print(f"My name is {name}. I am {age} years old. I am living in {city}.")
    
my_info(city="New Delhi", name="Mohan Kumar Mishra", age=34)

#! Default Parameter Value:---->
#* You can also set a default value if no argument is specified:

# examples:
# 1.
def my_info(name, city="Hathras"):
    print(f"Name is {name}. City is {city}.")

my_info("Ayushi Jain") 

#? Q1. What is a function in Python and why are functions used?
# *Answer: A function is a block of reusable code that performs a specific task. Functions make code modular, reusable, and easier to debug.

#? Q2. Differentiate between built-in functions and user-defined functions.
# *Answer:Built-in functions: Predefined in Python (len(), sum(), print()). User-defined functions: Created by programmers using def.

#? Q3. What is the difference between return and print() in a function?
def add_return(a, b):
    return a + b   # returns value

def add_print(a, b):
    print(a + b)   # only prints

print(add_return(3, 5))  # 8 (can be reused later)
add_print(3, 5)          # prints 8, but cannot reuse

#? Q4. Explain positional arguments and keyword arguments with an example.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Amit", 20)             # Positional
greet(age=22, name="Riya")    # Keyword

#? Q5. What are default arguments in Python functions?
def greet(name, msg="Good Morning"):
    print(f"Hello {name}, {msg}")

greet("Ankit")           # Hello Ankit, Good Morning
greet("Priya", "Hi!")    # Hello Priya, Hi!

#? Q6. What is the difference between local variables and global variables?
x = 10  # global

def func():
    x = 5  # local
    print("Inside:", x)

func()
print("Outside:", x)

#? Q7. What are *args and kwargs?
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Ravi", age=25)

#? Q8. What happens if a function does not include a return statement?
def hello():
    print("Hello World")

x = hello()
print(x)   # None

#? Q9. Can a function return multiple values? How?
def operations(a, b):
    return a+b, a-b, a*b

add, sub, mul = operations(5, 3)
print(add, sub, mul)  # 8 2 15

#? Q10. Explain lambda functions with an example.
square = lambda x: x*x
print(square(5))   # 25

#? Q11. Write a function add_numbers(a, b) that returns the sum of two numbers.
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 7))  # 10

#? Q12. Write a function is_even(n) that checks if a number is even.
def is_even(n):
    return n % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False

#? Q13. Write a function factorial(n) that returns the factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))  # 120

#? Q14. Write a function count_vowels(s) that returns the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print(count_vowels("Python Programming"))  # 4

#? Q15. Write a function reverse_string(s) that returns the reversed string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # olleh

#? Q16. Write a function fibonacci(n) that returns the first n Fibonacci numbers.
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]

#? Q17. Write a function find_max(lst) that returns the maximum number from a list.
def find_max(lst):
    return max(lst)

print(find_max([4, 9, 2, 15, 6]))  # 15

#? Q18. Write a function is_palindrome(s) that checks if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

#? Q19. Write a function calculate_area(shape, **kwargs) that calculates circle or rectangle area.
def calculate_area(shape, **kwargs):
    if shape == "circle":
        r = kwargs.get("radius", 0)
        return 3.14 * r * r
    elif shape == "rectangle":
        l = kwargs.get("length", 0)
        w = kwargs.get("width", 0)
        return l * w

print(calculate_area("circle", radius=5))        # 78.5
print(calculate_area("rectangle", length=4, width=6))  # 24

#? Q20. Write a lambda function to sort a list of tuples by the second element.
pairs = [(1, 3), (2, 1), (4, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(2, 1), (4, 2), (1, 3)]

#! Default Parameter Value:----->
#* You can also set a default value if no argument is specified:

# examples:
# 1.
def my_info(name, city="Hathras"):
    print(f"Name is {name}. City is {city}.")

my_info("Ayushi Jain")

# 2. 
def address(city, country="India"):
    print(f"City is {city}. Country is {country}.")

address("Hathras")
address("Hathras", "Russia")

#1 Passing List as an Argument:---->
#* You can send my data type of argument to a function (string, number, list, dictionary etc), and it will be treated as the same data type inside the function.

# example:
# 1. pass list as an argument
def fruits(fruit):
    for f in fruit:
        print(f)
        
fruitsList = ['apple', 'mango', 'banana', 'grapes', 'tindey']
fruits(fruitsList)

# 2. pass dictionary as an argument
def users(user):
    for key, value in user.items():
        print(key," : ",value)
        
user_data = {
    "id": 1,
    "name": "Mohan Kumar",
    "age": 34,
    "city": "New Delhi"    
}
users(user_data)

#! Recursion:---->
#* Recusion is a function that calls itself directly and indirectly.

# example:
# 1.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 
print(factorial(5))
#TODO: 5! = 5 * 4 * 3 * 2 * 1
