#! Sort Lists:-

#? Sort List Alphanumerically:-
#* List objects have a "sort()" method that will sort the list alphanumerically, ascending, by default.
# examples:
# 1.
fruits = ['mango', 'grapes', 'papaya', 'apple', 'pineapple']
fruits.sort()
print(fruits)

# 2.
alpha = ['y', 'T', 'Z', 'z', 'l', 'w']
alpha.sort()
print(alpha)

# 3.
nums = [9, 5, 8, 2, 0, 3]
nums.sort()
print(nums)

# 4. 
# mixed = [34, "ayushi", 'New Delhi', 89, "Mohan Lal", "agra"]
# mixed.sort()
# print(mixed)
#TODO: sort method list me likhe hue, alphabets or numbers ko ek sath sort nahi kar sakta.

# 5. use "reverse=True"
marks = [90, 65, 100, 178, 45, 25]
marks.sort(reverse=True)
print(marks)

# sort.(reverse=true) function use to sort in decending order 

# 6. use customize sort function:
"""def mySort(n):
    return abs(n - 10)

marks = [90, 65, 100, 178, 45, 25]
marks.sort(key=mySort)
print(marks)"""

# 7. case insensitive sort:
names = ["Mohan", "gopal", "Girdhari", "Anuradha"]
names.sort()
print(names)

# 8.
names = ["Mohan", "gopal", "Girdhari", "Anuradha", "anupam", 'anshi', "manohar"]
names.sort(key=str.lower)
print(names)

# 9. "reverse()" order:
count = [5, 3, 9, 2, 1, 8]
count.reverse()
print(count)

names.reverse()
print(names)