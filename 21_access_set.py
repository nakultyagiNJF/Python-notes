#! Access Items:-
#* We cannot access items in a set by referring to an index or a key.
#NOTE: But we can loop through the set items using a 'for' loop, or ask if a specified value is present in a set, by using the 'in' keyword.
# example:
# 1.
fruits = {'mango', 'grapes', 'papaya', 'pineapple'}
for fruit in fruits:
    print(fruit)   

# 2. using "in" keyword:-
print("pineapple" in fruits)

# 3. using "not in" keyword:-
print("grapes" not in fruits)

#! Add Items:-
#* Once a set is created, we cannot change its items, but we can add new items.

#? to add one item to a set use the `add()` method:
# example:
cities = {'hathras', 'agra', 'mathura'}
cities.add('new delhi')
print(cities) 

#! Add Sets:-
#? to add items from another set into the current set, use the `update()` method.
# example:
cities = {'hathras', 'agra', 'mathura'}  
new_cities = {'gokul', 'vrindavan', 'barsana'}
cities.update(new_cities)
print(cities)

#! Add Any Iterable:-
#* the object in the 'update()' method does not have to be a set, it can be any iterable object(tuples, lists, dictionaries etc.).
# example:
cities = {'hathras', 'agra', 'mathura'} # set
new_cities = ['barsana', 'vrindavan'] # list
cities.update(new_cities)
print(cities)

# example:
cities = {'hathras', 'agra', 'mathura'} # set
new_cities = ['barsana', 'vrindavan'] # list
New_cities = ('mumbai', 'delhi') # tuple
cities.update(new_cities, New_cities)
print(cities)
