#? Lists --- 
#* Lists are used to store multiple items in a single variable.
#* Lists are created using square brackets:
# example: here, i am create a list using square brakets:
fruits = ['apple', 'mango', 'banana', 'grapes'] # 1100101011 it is written randomly this binary is false
print(fruits) 

#? List Items ---
#* List items are ordered, changeable, and allow duplicate values.
#* List items are indexed, the first item has index [0], the second item has index [1] etc,
#* Index starts always 0.  

#? Ordered ---
#* When we say that lists are ordered, it means that the items have a defined order, and that order will not change.  
# If we add new items to a list, the new items will be placed at the end of the list. 

#? Changeble ---
#* The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#? Allow Duplicates ---
#* Since lists are indexed, list can have items with the same value:
# examples:
fruits = ['apple', 'mango', 'papaya', 'mango', 'grapes']
print(fruits) 


#?---List Length---
#* To determine how many items a list has, use the "len()" function:
findLength = ['ayushi', 'mohan', 'anupam', 'anuradha', 'mansu', 'meenakshi'] 
print(len(findLength)) 
# note: length - 1 = index | last index + 1 = length

#?---List Items - Data Types---
# examples:
# 1. store a single data type in a list:
names = ['mohan', 'sohan', 'rohan'] 
rolls = [1, 2, 3]
job = [True, False, True]
 
# 2. store multiple data types in a list:
info = [1, 'ayushi', 23, 'new delhi', True]

#?---type()--- here, i am using "type()" function.
# example:
# 1.
print(type(names))
print(type(info))

#?---The list() Constructor---
#* It is also possible to use the list() constructor when creating a new list.
# examples:
# 1.
names = list(('Mohan', 'Sohan', 'Anuj'))
print(names)
print(type(names))


#! Access List Items:-
#* List items are indexed and you can access them by referring to the index number.

#? Index ---
# examples:
# 1. here, using positive indexing:
fruits = ['apple', 'mango', 'banana', 'grapes' ] 
print(fruits[2])
print(fruits[3])

# 2. here, using negative indexing:
'''  fruits   ---   ['apple', 'mango', 'banana', 'grapes']  
    -ve index---      -4       -3       -2         -1'''
print(fruits[-2])
#TODO: negative indexing means start from the end '-1' refers to the last item, '-2' referes to the second last item, etc.


#? Range of Indexes ---
#* we can specify a range of indexes by specifying where to start and where to end the range.
# when specifying a range, the return value will be a new list with the specfied items.
# example:
# 1.
names = ['mohan', 'sohan', 'anuj', 'radhika', 'anuradha', 'anupam', 'mohit', 'gulshan']   
print(names[2:5])
# [startIndex : endIndex]

# 2.
print(names[:4])
#in this 4 character will not be taken

# 3.
print(names[3:])
# in this 3 will taken and after 3 character also taken

# 4.
print(names[-6:-1])
# [-veStartIndex : -veEndIndex]


#? Check if item Exists---
#* To determine if a specified item is present in list use the 'in' keyword:
# examples:
# 1.
names = ['mohan', 'sohan', 'anuj', 'radhika', 'anuradha', 'anupam', 'mohit', 'gulshan']
name = input("enter name using list : ")
if name in names:
    print("Yes")
else:
    print("No")