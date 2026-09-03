# ?Different Types of Errors
# Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program.

# Two types of Error occurs in python.

""" 
a. Syntax Errors
b. Logical Errors (Exceptions) 
"""

# Syntax Errors :

""" age = 18
if age < 18;
    print("Yes")
else:
    print("No") """
# note: syntax errors resolve nahi hoti hain.

# Logical Errors (Exceptions) :
# There are different types of logical errors:
""" 
    i. ZeroDivisionError:
    ii. NameError:
    iii. TypeError:
    iv. ValueError:
    v. IndexError:
    vi. KeyError:
    vii. ModuleNotFoundError:
    viii. ImportError:
"""

#* ZeroDivisionError

""" a = 0
divide = 1/a
print(divide) """
# output - ZeroDivisionError: division by zero

#* NameError

""" print(x) """ 
# here, x is not defined in this scope
# output - NameError: name 'x' is not defined
# note: yadi kisi bhi variable ko define karne se pahle use kar liya jaye to... output "variable" is not defined aata hai.

#* TypeError

""" l = 10
m = "20"
sum = l + m
print(sum) """
# output - TypeError: unsupported operand type(s) for +: 'int' and 'str'

#* ValueError

""" hi = int("eleven")
print(hi) """
# output - ValueError: invalid literal for int() with base 10: 'eleven'

#* IndexError

""" names = ["mohan", "sohan", "anuj", "gopal"]
print(names[4]) """
# output - IndexError: list index out of range

#* KeyError

"""user = {
"id": 1,
"name": "Tushar Sharma",
"age": 28
}
print(user["address"])"""
# output - KeyError: 'address'

#* ModuleNotFoundError

""" import mathhs """
# ModuleNotFoundError: No module named 'mathhs'
#* ImportError

#* Exceptional Handling
"""
    The 'try' block lets you test a block of code for errors.
    The 'except' block lets you handle the error.
    The 'else' block lets you execute code when there is no error.
    The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.
"""

# 1.
"""print("Start Code")
try:
    print(data)
except Exception as e:
    print(e)
print("End Code")"""

""" print("start") 

def hello():
    print("Hello Helllo")
    
try:
    def sayhi():
        print(Hello Shree)
    sayhi()
except Exception as e:
    print(e)  """  

# 2.
""" print("Start Code")
try:
    print(info)
except:
    print("An error occurred")
print("End Code") """

# 3.
""" print("Start Code")
try:
    i = "9"
    j = 10
    add = i + j
    print(add)
except TypeError:
    print("Invalid input. Please enter numeric values.")
print("End Code") """

# 4.
""" print("Start Code")
try:
    print("Done")
except Exception as e:
    print(e)
else:
    print("No error occurred")
print("End Code") """

# 5.
""" print("Start Code")
try:
    print("Done")
except Exception as e:
    print(e)
else:
    print("No error occurred")
finally:
    print("Always executed")
print("End Code") """