#! Copy Lists:

#? Copy a List:-
# examples:
#* 1.
"""org = ['apple', 'pineapple', 'papaya', 'grapes'] # 100011001
copy = org # 100011001 ❌
print("org list : ", org)❌
print("copy list : ", copy)❌

# after change in copy list:
copy.append("banana")❌
print("after change org list : ", org)❌
print("after change copy list : ", copy)❌"""

#* 2. here, first solution: use "copy()" method:-
"""org = ['apple', 'pineapple', 'papaya', 'grapes'] # 1101010101
copy = org.copy() # 1101011101

print("org list : ", org)
print("copy list : ", copy)

# after change in copy list:
copy.append("banana")
print("after change org list : ", org)
print("after change copy list : ", copy)"""

#* 3. here, second solution: use "list()" function (constructor function):
"""org = ['apple', 'pineapple', 'papaya', 'grapes'] # 1101010101
copy = list(org) # 1101011101

print("org list : ", org)
print("copy list : ", copy)

# after change in copy list:
copy.append("banana")
print("after change org list : ", org)
print("after change copy list : ", copy)"""

#* 4. use the slice operator:
"""org = ['apple', 'pineapple', 'papaya', 'grapes'] # 1101010101
copy = org[:] # 1101011101

print("org list : ", org)
print("copy list : ", copy)

# after change in copy list:
copy.append("banana")
print("after change org list : ", org)
print("after change copy list : ", copy)"""

# These are the real code :-
org = ['apple', 'pineapple', 'papaya', 'grapes']
copy = org.copy()
copy.append("banana")
print(copy)

copy = list(org)
copy.append("Anupam Joshi")
print(copy)

copy = org[:]
copy.append("banana")
print(copy)