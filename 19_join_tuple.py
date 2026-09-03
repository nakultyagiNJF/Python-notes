#! Join Tuples:-

#? to join two or more tuple we can use the "+" operator.
# example:
fruit_1 = ('mango', 'grapes')
fruit_2 = ('papaya', 'pineapple')
fruit_3 = list((fruit_1))
fruit_4 = list((fruit_2))
fruit_3.extend(fruit_4)
fruit_1 = tuple((fruit_3))
fruit_2 = tuple((fruit_4))
print(fruit_1)


all_fruits = fruit_1 + fruit_2   
print(all_fruits)

#? mutiply tuple:
# example:
fruits = ('mango', 'grapes')
manyFruits = fruits * 2
print(manyFruits)

#! Tuple Method:-

#? 1. .count():-
#* the `count()` method returns the number of times a specifed value appears in the tuple.
# example:
# 1.
numbers = (1, 4, 2, 3, 6, 2, 3, 4, 2, 2, 6, 6, 6) 
print(numbers.count(2))  

# 2.
names = ('mohan', 'sohan', 'mohan', 'anuj', 'ayushi', 'mohan')
print(names.count('mohan'))

#? 2. .index():-                                                                                     
# example:
# 1.
names = ('mohan', 'sohan', 'anuj', 'ayushi')
print(names.index('ayushi'))