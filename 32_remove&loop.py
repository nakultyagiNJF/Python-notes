#! Remove Dictionary Items:-
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}  

#? using "pop()" method: removes specific keyvalue.
user.pop('name')
print(user)

#? using "popitem()" method: removes the last inserted item.
user.popitem()
print(user) 

#? using "del" keyword:
# del user["city"]
# print(user)
# NOTE: "del" keyword can also delete the dictionary completly:
# del user
# print(user)

#? using "clear()" method:
user.clear()
print(user)


#! Loop Through a Dictionary:
#* We can loop through a dict by using a "for" loop.
# When looping through a dict, the return values are the 'keys' of the dict, but there are methods to return the 'values' as well.
# examples:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age' : 34,
    'city': 'New Delhi'
}  

for key in user:
    print(key)  
# NOTE:print keys only 

for y in user:
    print(user[y])
# NOTE:print values only

#? here are using some methods like "keys" and "values"
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
} 

#* using "keys" method:
for key in user.keys():
    print(key) 
# NOTE:print keys only    

#* using "values" method: 
for value in user.values():
    print(value) 
# NOTE:print values only    

#? get keys and values both:--- using "items()" method:
for key, value in user.items():
    print(f"{key} : {value}")