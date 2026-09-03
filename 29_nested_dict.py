#! Nested Dictionaries:-
#* A dict. can contain dictionaries, this is called nested dict.

#? how to create a nested dict:-?
# example:
# 1.
family = {
    "child1" : {
        'name': 'Deepak',
        'age': 23
    },
    "child2" : {
        'name': 'Chanda',
        'age': 21
    },
    "child3" : {
        'name': 'Akash',
        'age': 18
    }
}  

# 2.
""" child1 = {
        'name': 'Deepak',
        'age': 23
}
child2 = {
        'name': 'Chanda',
        'age': 21
}
child3 = {
        'name': 'Akash',
        'age': 18
}
family = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}   """ 

#? how to access nested dict:-? 
print(family["child3"]["name"])
print(family["child2"]["age"])

#? loop through:-?
for x, obj in family.items():
    for y in obj:
        print(f"{y} : {obj[y]}")

for y, sys in family.items():
    for x in sys:
        print(f"{x} : {sys[x]}")     