#! Python Iterators:----->>
#* An iterator is an object that contains a countable number of values.
#* An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. 

#* Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.

#? Iterator vs Iterable?
#* Lists, tuples, dictionaries, and  sets are all iterable objects. They are iterable containers which you can get an iterator from.
#* All these objects have a `iter()` method, which returns an iterator object.

# examples:---->>
# 1.
myTuple = ('apple', 'mango', 'papaya', 'pineapple')
myItem = iter(myTuple)

print(next(myItem))
print(next(myItem))
print(next(myItem))
# print(next(myItem))

# print(next(next(myItem))) # error, because it retuns string data type.

item = next(myItem)
print(type(item)) # str

# 2.
your_name = "Ayushi Sharma"
name = iter(your_name)

print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))

#? Looping Through an Iterator:---->>
#* You can loop through an iterator by using a `for` loop.
# 3.
myTuple = ('apple', 'mango', 'papaya', 'pineapple')

for item in myTuple:
    print(item) 
    
# 4.
your_name = "Ayushi Sharma"

for char in your_name:
    print(char)