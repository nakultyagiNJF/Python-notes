#! Dictionary:-
#* Dictionaries are used to store data values in key:value pairs.
#* A dictionary is a collection which is ordered*, changeable and do not allow duplicates. 
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
print(user)
 
 
#TODO:- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. 

#! Dictionary Items:-
#* Dictionary items are ordered, changeable, and do not allow duplicates.
#* Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
print(user['name'])

#! Dictionary Length:-
#* To determine how many items a dictionary has, use the len() function:
# example:
print(len(user))

#! Get data type:
# using "type()" method:
# example:
print(type(user)) 

#! The "dict()" Constructor:-
#* It is also possible to use the dict() constructor to make a dictionary.
# example:
info = dict(name="Ayushi Jain", age=29, city="Agra")
print(info)