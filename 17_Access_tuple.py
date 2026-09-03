#! Access Tuple Items:-
#* We can access tuple items by referring to the index number, inside square brackets.
# examples:
# 1. using `+ve` indexing:
fruits = ("apple", "mango", "grapes", "papaya")
print(fruits[2])

# 2. using `-ve` indexing:
print(fruits[-3])

#! Range of Indexes:- {like: a slicing}
#* We can specify a range of indexes by specifying where to start and where to end the range.
# examples:
# 1. using "+ve" indexing:
names = ('sohan', 'mohan', 'anuj', 'gopal', 'tushar', 'ayushi', 'madhavi', 'mannu', 'anju')
print(names[1:5])
# [startIndex : endIndex]
# return's new tuple.

# 2.
print(names[:5])

# 3.
print(names[2:])

# 4. using "-ve" indexing:
print(names[-6:-2])

#! Check if item Exists:
#* to determine if a specified item is present in a tuple use the `in` keyword:  
fruits = ("apple", "mango", "grapes", "papaya")
print("papaya" in fruits)