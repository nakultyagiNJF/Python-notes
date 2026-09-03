#! Tuple:-
"""
    *Tuples are used to store multiple items in a single variable.
    *A tuple is a collection which is `ordered` and `unchangeable`.
    *Tuple are written with `round brackets` aka parenthesis
""" 
# examples:
# 1.
my_fruits = ("apple", "mango", "grapes", "papaya")
print(my_fruits)
print(type(my_fruits))

#! Tuple Items:-
"""
    *Tuple items are ordered, unchangeable, and allow duplicate values.
    *Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
""" 

#? Ordered-----
#TODO: When we say that tuple are ordered, it means that the items have a defined order, and that order will not change.
#? Unchangeable----
#TODO: Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#? Allow Duplicate----
#TODO: Since tuples are indexed, they can have items with the same value.
# example:
names = ('mohan', 'sohan', 'anuj', 'gopal', 'sohan')
print(names)       

#! Tuple Length:-
#* To determine how many items a tuple has, use the `len()` function
# example:
my_fruits = ("apple", "mango", "grapes", "papaya")
print(len(my_fruits))

#! Create Tuple With One Item:-
single_name = ("Ayushi",)
print(single_name)
print(type(single_name)) 
#NOTE: to create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

#! Assign Multiple Data Types in a Single Tuple:-
user = (1, "Ayushi Gupta", "Noida", 8881126429, True)
print(user)
print(type(user))

#! The `tuple()` Constructor:-
#* It is also possible to use the `tuple()` constructor to make a tuple.
random = tuple(('a', 'b', 'c', 'd', 'e'))
print(random)