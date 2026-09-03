#! Join Sets:-
""" 
    -There are several ways to join two or more sets in Python:

    *1. The `union()` and `update()` method joins all items from both sets.
    *2. The `intersection()` method keeps ONLY the duplicates.
    *3. The `difference()` method keeps the items from the first set that are not in the other set(s).
    *4. The `symmetric_difference()` method keeps all items EXCEPT the duplicate.
"""

#? Union:-
#* The 'union()' method returns a new set with all items from both sets.
# example:
set_num = {1, 4, 7, 6}
set_alpha = {'f', 'y', 'k', 'e'}
join_set = set_num.union(set_alpha)
print(join_set) 

#* We can use the '|' operator insted of the `union()` method, and we will get the same result.
# example:
set_num = {1, 4, 7, 6}
set_alpha = {'f', 'y', 'k', 'e'}
join_set = set_num | set_alpha
print(join_set)

#* join multiple sets.
# example:
set1 = {'a', 'b', 'c'}
set2 = {1, 7, 4}
set3 = {'sohan', 'mohan', 'anuj'}
set4 = {'delhi', 'agra', 'hathras'}

join_all_set = set1.union(set2, set3, set4) # using 'union()' method
print(join_all_set) 

join_all_set = set1 | set2 | set3 | set4 # using '|' operator
print(join_all_set)

#* Join a Set and a Tuple. 
# example:
names = {'sohan', 'mohan', 'anuj'} # set
cities = ('agra', 'mathura', 'delhi') # tuple
names_cities = names.union(cities)
print(names_cities)

# if we are joining two different set like list nd tuple we will use .union() method only any symbol will not work 

#? Update:-
#* the 'update()' method insert all items from one set into another. the 'update()' change the original set, and does not return a new set. 
# examples:
names = {'sohan', 'mohan', 'anuj'} 
cities = {'agra', 'mathura', 'delhi'} 
names.update(cities)
print(names)

#TODO: Both 'union()' and 'update()' will exclude any duplicate items.

#? Intersection:-
#* Keep ONLY the duplicates.
#* The `intersection()` method will return a new set, that only contains the items that are present in both sets.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
new_set = set1.intersection(set2)
print(new_set)  

#* we can use the '&' operator inseted of the `intersection()` method, and we will get the same result.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
new_set = set1 & set2
print(new_set) # returns new set

#* the `intersection_update()` method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
set1.intersection_update(set2)
print(new_set) # not returns new set

#? Difference:-
#* the `difference()` method will return a new set that will contain only the items from the first set that are not present in the other set.  
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
new_set = set1.difference(set2)
print(new_set)

#* we can use the '-' operator.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
new_set = set1 - set2
print(new_set)

#* the `diffence_update()` method will also keep the items from the first set that are not in the other set, but it will change the original set inseted of returning a new set.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
set1.difference_update(set2)
print(set1)

#? Symmetric Differences:-
#* the `symmetric_difference()` method will keep only elements that are NOT present in BOTH sets.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
new_set = set1.symmetric_difference(set2)
print(new_set)

#* we can use the '^' operator insted of the `symmetric_difference()` method, and we will get the same result.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
new_set = set1 ^ set2
print(new_set)

#* the `symmetric_difference_update()` method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
# example:
set1 = {'apple', 'mango', 'grapes'}
set2 = {'pineapple', 'grapes', 'apple'}
set1.symmetric_difference_update(set2)
print(set1)

# In my language 
# union will join the two set and give the output in new set, we can also use | for union.
# update will also join two set but will not give the output in new set it will take the first variable for joining.
# intersection will make a new set and in that there will be only dublicate values, you can also use & for intersection. 
# intersection_update do not need new variable it will update in first variable only. 
# difference will make new set and in that there will be non dublicate value and only first variable value will come in new set, you can use - for difference.
# difference_update do not need new variable it will update in new variable only. 
# symmetric_difference will make a new set and in that there will be non dublicate value from both set, you can use ^ for symmetric_difference.
# symmetric_difference_update do not need new variable it will update in first variable only.    
