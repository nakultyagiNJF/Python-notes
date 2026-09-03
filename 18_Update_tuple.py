#! Update Tuple:-
""" 
    *Once a tuple is created, we cannot change its values. Tuples are unchangeable, or immutable as it also called.
    *But there is a workaround.
    *--We can convert the tuple into a list, change the list, and convert the list back into a tuple.
""" 
# example:
t_names = ('sohan', 'mohan', 'anuj', 'gopal')
l_names = list(t_names)
l_names.append('ayushi')

t_names = tuple(l_names)
print(t_names)
print(type(t_names))

#TODO: baaki, insert karna, append karna, remove karna etc, aap tuple ko list me convert kar ke kar sakte ho. same as list.
#! Unpacking a Tuple:-
#* When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
# example:
fruits = ('apple', 'mango', 'grapes')

#* But, in Python, we are also allowed to extract the values back into values. This is called "unpacking".
# example:
fruits = ('apple', 'mango', 'grapes')
(f1, f2, f3) = fruits
print(f1)
print(f2)
print(f3)

#! Using Asterisk(*) :-
# example:
# 1.
names = ('mohan', 'sohan', 'anuj', 'gopal', 'tushar', 'ayushi', 'anupam', 'anuradha', 'madhavi')
(n1, n2, n3, *n_all) = names
print(n1) 
print(n2) 
print(n3) 
print(n_all)

print(f"These people come to my office right now: {n_all}")

print(n_all) 
print(type(n_all))
# return's new list.

# 2.
(n1, *n_all, n3, n4) = names
print(n1)
print(n_all)
print(n3)
print(n4)

#! Loop Through:-

#? 'for' loop:-
# example:
fruits = ('apple', 'mango', 'grapes')
for fruit in fruits:
    print(fruit) 

#? using `range()` nd `len()`:-
# example:
fruits = ('apple', 'mango', 'grapes')
for i in range(len(fruits)):
    print(fruits[i])

#? using 'while' loop:-
# example:
fruits = ('apple', 'mango', 'grapes')
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1