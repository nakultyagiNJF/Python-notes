# Class and Object :-
"""
    * Everything in Python is an object. An object has a state and behaviors.
    * To create an object, you define a class first.
    * And then, from the class, you can create one or more objects.
    * The objects are instances of a class.
"""

# define a class:
# To define a class, you use the class keyword followed by the class name.
class Person:
    pass

# create an object:
# To create an object from the Person class,
# you use the class name followed by parentheses (), like calling a function:
person = Person()
# NOTE:- the person is an instance of the Person class. Classes are callable.

'''more examples:----'''
# 1.
# create 'User' name class:
class User:
    name = "Tushar Sharma"
    age = 23
    city = "Noida"

# create 'user' name object:
user = User()
print(f"My name is {user.name}. I am {user.age} years old. I am living in {user.city}.")

# create another object with 'ano_user' name:
ano_user = User()
ano_user.name = "Mohan Mishra"
ano_user.age = 34
ano_user.city = "Agra"
print(f"My name is {ano_user.name}. I am {ano_user.age} years old. I am living in {ano_user.city}.")

name = User()
name.name = "gautami shukla"
name.age = 22
name.city = "delhi"
print(f"My name is {name.name}. I am {name.age} years old. I am living in {name.city}.")


        