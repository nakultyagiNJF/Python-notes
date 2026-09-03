#! String :----------------
""" 
    *String in python are surrounded by either single or double quotation marks.
    *like as: 'Hello' is the same as "Hello".
    *we can display a string literal with the `print()` function.
""" 

# example:
print("Hello")
print('Hello')

#* Quotes Inside Quotes :------------
# you can use quotes inside a string, as long as they don't match the quotes surrounding the string:
""" 
    ?Note: - double quotes ke under double quotes nahi aa sakte or single ke under single nahi aa sakte. marked--- double quotes ke under single quotes aa sakte hain or single ke under double aa sakte hain.
"""

# examples:
print("It's alright")
print('He is called "Tushar"')

# print("Hello"s Shree!") ❌
# print('Hello's Shree!') ❌

#*  Multiline Strings :--------------
# you can assign a multiline string to a variable by using three quotes:"""
info = """
name : "Tushar Sharma"
age : 45
city : "New Delhi"
"""
print(info)

#! String are Array :----------------- 
name = "Tushar"
print(name)

"""
    name - t u s h a r
   index - 0 1 2 3 4 5 
  length - 1 2 3 4 5 6
   
    index - length - 1
"""
print(name[2])
print(name[0])

#* looping through a string:
for letter in name:
    print(letter)
    
'''
    * string ko iterate karne ke liye maine 'for' loop ka use kiya hai,
    jisme:
         
         -for- loop hai,
         -letter- vah variable hai jisme name ka ek-ek character temparory store hoyenge,
         -in- yah loop ki help karta hai ki "is string me se character nikalo"
         -name- yah to aap janta hi hain, ye string hai,
         -:- semicolon lagane se python me block start ho jata hai,
         -print(letter)- ye name ke ek-ek letter ko print karne ke me helpful hai.
         '''

#! String Lenght :-------------
sen = "Hello Ayushi" 
sen = "meenakshi"
print(len(sen)) 
''' 
   - to get the length of a string, use the 'len()' function. 
'''

#! check String :--------------
# TO Check if a certain phrase or character is present in string, we can use the keyword 'in':
txt = "the best things in file are free!"
print("free" in txt)

print("best" not in txt)


#? Assign String to a Variable --
# examples:
name = "Tushar Sharma" 
print(name) 


#? Multiline Strings --
# examples:
info = """
name : Ayushi Jain
age : 32
city : Hathras City
phone : 8881126429
""" 
print(info)


#? String are Arrays --
# examples:
name = "Anupam"
print(name[2])

# note: basically, jab bhi aap koi string, list, tuple banate hain to aap unke kisi bhi element ya character ko nikal sakte hain, means single use kar sakte hain.

#? Looping Through a String --
# here, i am using "for" loop for iterate string characters.
for e in name:
      print(e) 

#? String Lenght --
# now, i am using "len()" function for get the string length.
sen = "I love Python Language."
print(len(sen)) 


#? Check String --
# now, i am using "in" for check string.
print("Love" in sen)


#! Python Slicing Strings :->
#* We can return a range of characters by using the slice syntax.
#* Specify the start index and the end index, separated by a colon, to return a part of the string.   

# examples:
# 1.
sayHi = "Hello Shree!"
print(sayHi[3:8])
# note: [startIndex : endIndex]

# bring out the first and last 3 character from the string 
#example

#1 first character
print(sayHi[:1])

#2 last 3 character
print(sayHi[9:12])
print(sayHi[9:])

# in this 9th character will be taken and after 9th characters also taken

# 2. 
print(sayHi[:9])
# note: [ : endIndex]
#in this 9th character will not be taken

# 3.
print(sayHi[2:])
# note: [startIndex : ]

# 4.
print(sayHi[0:12:2])
# note: [startIndex : endIndex : step]
# In this 12 is the lenght of the string and 2 is used to give nunber of character you have to miss and 0 is starting index of the string. 


#! String Modify :-

#* 1. Upper Case:
# using "upper()" function:
sen = "I love Python Programming Language"
print(sen.upper()) 

# using "lower()" function:
print(sen.lower())

# using "strip()" function for using remove whitespace:
trm = "Hello World!     "
print(trm.strip())

# using "split()" function for using convert string into list:
data = "Hello Shree, How can i help you?"
print(data.split())

# using "capitalize()" function for making first letter capital and other letter small:
user = "hello world"
print(user.capitalize())

# !concatination:--

# example :--
f_name = "Tushar"
l_name = "Sharma"

full_name = f_name + l_name
print(full_name)

# example :--
f_name = "Tushar"
l_name = "Sharma"

full_name = f_name + " " + l_name
print(full_name)

# advanced:
full_name = f"{f_name} {l_name}"
print(full_name)

#! Python Format String :--

#? problem:-- 
# examples: 1.
name = "Nakul Tyagi"
age = 19
city = "Najafgarh"

full_detail = "My name is " + name +"I am " + str(age) + "years old." + "I am living in " + city
print(full_detail)

#? solution: f-string:-- 
full_detail = f"My name is {name}. I am {age} years old. I am living in {city}."
print(full_detail)

# examples: 2.
sName = "Anurag Sharma"
marks = 325
per = marks/500*100
print(f"Student name is {sName}. Marks is {marks}. and Percentage is {per:.2f}.")

#! Escape Characters:--
"""
    \'  -  single quote
    \\  -  backslash
    \n  -  new line
    \t  -  tab
""" 

# examples:
sen = 'I love \'Python\' Programming Language'
print(sen)

info = "\tName is Tushar.\nAge is 34.\nCity is New Delhi."
print(info)

demo = "I love Python\\JavaScript Language."
print(demo)