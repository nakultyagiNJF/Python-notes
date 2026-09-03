# **Scopes**
# *there are two types of scopes in python :
# **1. Global Scope** : variables defined outside a function are known as global variables. They can be accessed from anywhere in the program.

glb = "Hello Shree" # it's a global scope, it's a global variable

def change():
    print("function : ", glb)
change()

print("global : ", glb)
# **2. Local Scope** : a variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def lcl():
    l_var = "Local Scope"
    print("local : ", l_var)
lcl()

# print(l_var)
# Some Eg for better understanding the scopes :
a = "Hello Shree!" # global variable/ global scope

def demo():
    a = "Hi Shree!" # local variable/ local scope
    print(a)
demo()

print(a)
name = "Tushar Sharma"

def re_name():
    global name
    name = "Ajit Gautam"
re_name()

print(name)

one = "One"

def outer():
    two = "Two"

    def inner():
        three = "Three"
        print(one)
        print(two)
        print(three)
    inner()

    print(one)
    print(two)
    # print(three)

outer()

print(one)
# print(two)
# print(three)