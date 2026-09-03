#! Set?
#* Sets are used to store multiple items in a single variable.
#* A set is a collection which is `unordered`, `unchangeable`, and `unindexed`.
#NOTE: Set items are unchangeable, but we can `remove` items and add new items.
#* Sets are written with curly brackets.
# example:
fruits = {'mango', 'grapes', 'papaya'}
print(fruits)     

#! Set Items:-
#* Set items are 'unordered', 'unchangeable' and 'do not allow duplicate' values.

#? unordered :-
"""
    *Unordered means that the items in a set do not have define order.
    *Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
"""
#? unchangeable:-
"""
    *Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    NOTE: Once a set is created, we cannot change its items, but we can remove items and add new items.
"""
#? do not allow duplicate:-
"""
    *Set cannot have two items with the same value.
"""
# example:
fruits = {'mango', 'grapes', 'papaya', 'mango', 'grapes'}
print(fruits)

#NOTE: the value 'True' and '1' are considered the same value in sets, and are treated as duplicate.
# example:
nums = {True, "Hello", 1}
print(nums) 

#! Get the Length of a Set:-
#* use the "len()" function.
# example:
names = {'mohan', 'sohan', 'anuj', 'gopal'}
print(len(names))  

#! Set Items - Data Types:-
# examples:
set1 = {'mango', 'grapes', 'papaya'}
set2 = {1, 5, 3, 8, 9}
set3 = {True, False, True}
print(type(set1), type(set2), type(set3)) 

#! The "set()" Constructor:-
#* It is also possible to use the "set()" constructor to make a set.
# example:
cities = set(('new delhi', 'agra', 'mathura', 'gokul', 'hathras'))
print(cities)
print(type(cities))