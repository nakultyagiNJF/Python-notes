#! Loop Lists: 

#? Loop Through a List:-
#* We can loop through the list items by using a 'for' loop.

# examples:
# 1.
"""fruits = ['apple', 'mango', 'papaya', 'grapes']
for e in fruits:
    print(e)"""
#TODO: yahan, "e" variable me list ke items temporary mode me store hote hain, means jaise jaise loop chalega vaise vaise "e" ki value change hogi.

#? Loop through the index numbers:
#* We can also loop through the list items by referring to their index number.
#* Use the 'range()' and 'len()' functions to create a suitable iterable.   

# 2.
"""fruits = ['apple', 'mango', 'papaya', 'grapes']
for i in range(len(fruits)):
    print(fruits[i])"""

# To reverse the list using for loop
"""nums = [10, 20, 30, 40, 50]

for x in nums[::-1]:
    print(x)"""
    
# To write a loop to print only the names that start with 'A'.
"""names = ["Amit", "Raj", "Priya", "Sneha", "Vikas", "Anita"]

for name in names:
    if name.startswith("A"):
        print(name)"""
        
"""names = ["Amit", "Raj", "Priya", "Sneha", "Vikas", "Anita"]

for name in names:
    if name.endswith("a"):
        print(name) """       

#TODO: yahan, "i" variable me index values store hogi, jaise first hoga '0' index or 0 index par 'apple' item hai to vo sabse pahle 0 index ki value display karega and again index change hote hote list ke sare items iterate ho jayenge.

#? Using a While Loop:
# 3.
"""names = ['mohan', 'sohan', 'anuj', 'gopal']
i = 0
while i < len(names):
    print(names[i])
    i+=1"""

#? Looping Using List Comprehension:
#* List Comprehension offers the shortest syntax for looping through lists.
# 4.
"""names = ['ayushi', 'anuradha', 'madhavi', 'madhu', 'meenakshi']
[print(item) for item in names]"""

#TODO: basically, yah ek looping/iteration ka shorthand hai, jiska use karke aap apne code/syntax ko kaffi hadd-tak short kar sakte ho, jisse code complexity kam hoti hai.-------

#! List Comprehension:
#* List Comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# examples:
# 1. 
"""names = ['ayushi', 'anuradha', 'madhavi', 'madhu', 'meenakshi']
new_names = []
# long way-
for e in names:
    if "m" in e:
        new_names.append(e)
print(new_names)"""


# short way- [expression for item in iterable if condition == True]
"""new_names = [item for item in names if "i" in item]
print(new_names)"""

''' explaination:
        item ---- print the items
        for item in names ---- for loop
        if "i" in item ---- condition
'''
#? Iterable:
# examples:
# 1. here, i am using "range()" function.
"""new_count = [num for num in range(11)]
print(new_count)"""

# 2. 
"""[print(num) for num in range(11)]"""

# if we directly print the code it will iterate the list....
# if we make list then print the code we will get list in the terminal.
 
"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(num)
print(total)"""

#? to add, multiply and etc in list. use this for loop method:------
 
"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_num = 0
for x in num:
    new_num += x
print(new_num)"""
