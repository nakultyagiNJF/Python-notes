#! Copy Dictionaries:-

# example:
# 1.
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
} # 1101010101

ano_user = user # 1101010101

print("user - ", user)
print("ano_user - ", ano_user)

# after changes in ano_user:
ano_user["skill"] = "React-JS"
 
print("after change user - ", user)
print("after change ano_user - ", ano_user)

#? using "dict()" function:---
user = {
    'id': 1,
    'name': 'Mohan Kumar',
    'age': 34,
    'city': 'New Delhi'
} # 1101010101

ano_user = dict(user) # 1101010111

print("user - ", user)
print("ano_user - ", ano_user)

# after changes in ano_user:
ano_user['skill'] = "React-JS"
 
print("after change user - ", user)
print("after change ano_user - ", ano_user)
