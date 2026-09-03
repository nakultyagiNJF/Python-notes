#! Accessing Items:-
#* You can access the items of a dictionary by referring to its key name, inside square brackets:
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
print(user['id'])
print(user['name'])

#? There is also a method called get() that will give you the same result:
# example:
data = user.get("city")
print(data)

#? Get Keys:----
#* The keys() method will return a list of all the keys in the dictionary. 
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
keyss = user.keys()
print(keyss)

#? Get Values:----
#* The values() method will return a list of all the values in the dictionary. 
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
valuess = user.values()
print(valuess)

#? Get Items:----
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
ittems = user.items()
print(ittems)