#! Remove Item:-
#? to remove an item in a set, use the `remove()`, or the `discard()` method.
# examples:
# 1. `remove()` :-
cities = {'hathras', 'agra', 'mathura', 'noida', 'delhi', 'dwarka'}
cities.remove("noida")
print(cities)

#NOTE: if the item to remove does not exist, 'remove()' will raise an error. 
# cities.remove("new delhi")
# print(cities) # KeyError: 'new delhi'

# 2. `discard()` :-
cities = {'hathras', 'agra', 'mathura', 'noida', 'delhi', 'dwarka'}
cities.discard("mathura")
print(cities)

#NOTE: if the item to remove does not exist, 'discard()' will NOT raise an error.
# cities.discard("new delhi")
# print(cities) # return current set

#? we can also use the `pop()` method to remove an item, but this method will remove a random item, so we cannot be sure what item that gets removed. The return value of the `pop()` method is the removed item.
# example:
cities = {'hathras', 'agra', 'mathura', 'noida', 'delhi', 'dwarka'}
rm_value = cities.pop()
print(cities)
print(rm_value) # returns removed value
#NOTE: sets are 'unordered', so when using the "pop()" method, we do not know which item that gets removed.

#? `clear()` :-
# example:
cities = {'hathras', 'agra', 'mathura'}
cities.clear()
print(cities)

#? `del` keyword for delete set completely :-
# example:
"""cities = {'hathras', 'agra', 'mathura'}
del cities
print(cities)""" # NameError: name 'cities' is not defined

#! Loop Items:-
#* we can loop through the set items by using a 'for' loop:
# example:
cities = {'hathras', 'agra', 'mathura'}
for city in cities:
    print(city)