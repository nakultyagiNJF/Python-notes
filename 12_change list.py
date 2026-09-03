#! Change List Items :-

#? Change Item Value:
#* change the value of a specific item, refer to the index number.
# examples:
# 1.
fruits = ['mango', 'papaya', 'grapes', 'apple']
fruits[1] = "pineapple"
print(fruits)

# 2.
fruits[3] = "banana"
print(fruits)


#? Change a Range of Item Values:
# examples:
# 1.
names = ['mohan', 'sohan', 'anuj', 'radhika', 'anuradha', 'anupam', 'mohit', 'gulshan']
names[1:4] = ["AYUSHI", "ANSHIKA", "AANVI"]
print(names)
#TODO:- jab bhi aap list me se kisi range ke elements ko update karte ho to re-assigning process assign ki gayi value ko bhi ek new list me hi likha jata hai, chahe vo ek single value ho ya multiple values. 

# 2.
names[6:7] = ["SHUBH"]
print(names)

# 3. 
names[6:7] = ["SHUBH", "KARAN", "ARJUN", "DURYODHAN", "MAMA-SHAKUNI"]
print(names)

#? 1. Insert Items:
#* To insert a new item, without replacing any of the existing values, we can use the "insert()" method.
#* The "insert()" method inserts an item at the specified index:
#* examples:
# 1.
num = [1, 2, 3, 4, 5]
num.insert(3, "seven")
print(num)

# 2.
fruits = ['mango', 'papaya', 'grapes', 'apple']
fruits.insert(3, "watermelon")
print(fruits)
#NOTE: as a result of the exmple above, the list will now contain 5 items. 

# 3.
alpha = ['a', 'b', 'c', 'd']
alpha.insert(4, "E")
print(alpha)
#TODO: insert() method ka jab bhi aap use karte hain to, aap single value hi insert kar sakte ho multiple nahi, or yahan aap ko index number bhi likhna hota hai.


#! Add List Items:-

#? 1. Append Items:
#* to add an item to the end of the list, use the 'append()' method:
# examples:
# 1.
num = [1, 2, 3, 4, 5]
num.append("six")
print(num)

num.append("end")
print(num)

#? 3. Extend List:
#* to append elements from another list to the current list, use the "extend()" method.
# examples:
# 1.
num = [1, 2, 3, 4, 5]
ano_num = [6, 7, 8, 9]
num.extend(ano_num)
print(num)


#! Remove List Items:-

#? remove specified item:
# to use "remove()" method.
# examples:
# 1.
alpha = ['a', 'b', 'c', 'd']
alpha.remove('c')
print(alpha)

# 2.
alpha = ['E', 'B', 'C', 'A', 'D', 'A']
alpha.remove("A")
print(alpha)

# 3.
alpha = [1, 2, 3, 4, 5, 6]
alpha.remove(2)
print(alpha)

#? remove spcified index:
#* the "pop()" method removes the specified index.
# examples:
# 1.
alpha = ['a', 'b', 'c', 'd']
alpha.pop()
print(alpha)
#TODO: yadi aap pop() method me koibhi index nahi daalte to vah last index ki value ko remove kar deta hai.

alpha.pop(1)
print(alpha)
#TODO: yadi aap index daalte ho to vah usi index ki value ko remove karta hai.

#? "del" keyword: 
# examples:
# 1.
alpha = ['a', 'b', 'c', 'd']
del alpha[3]
print(alpha)

""" del alpha
print(alpha) """

#? clear the list:
# examples:
# 1.
alpha = ['a', 'b', 'c', 'd']
alpha.clear()
print(alpha)

