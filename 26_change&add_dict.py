#! Change Dictionary Items:-
#* You can change the value of a specific item by referring to its key name:
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
user['name'] = "Ayushi Verma"
print(user)

#! Update Dictionary:-
#* The update() method will update the dictionary with the items from the given argument.
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}
user.update({'age':45})
print(user)

#! Add Dictionary Items:-
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
}  
user['job'] = True
print(user)

#! Update Dictionary:-
# example:
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
} 
user.update({'skill': 'Doctor'})
print(user)



