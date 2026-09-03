# !Control Statement :-

""" There are different types:
        ?1. Conditional Statement
            i. if
            ii. if else  
            iii. elif
            iv. if elif else
            v. nested if elif else

        ?2. Looping Statement
            i. while loop
            ii. for loop
            iii. break
            iv. continue
"""

# ?1. Conditional Statement :--------------------------------
# *i. "if" statement:
# examples:
""" age = 18
if age >= 18:
    print("You are eligible for voting!")

time = 14
if time >= 12 and time <= 16:
    print("Good Afternoon")

count = 3
if count < 4:
    print("Big number!!") """

# *ii. if else:
# examples:
""" age = 19
if age >= 18:
    print("you are eligible for voting!")
else:
    print("you are not...!")""" 

"""que = "Yes"
print("Kya aap sone ja rahe hain?(Yes or No) : ", que)
if que == "Yes":
    print("Good Night!")
else:
    print("Good Evening!")"""

"""print("Kya aap sone ja rahe hain?(Yes or No) : ")
decision = (input("enter decision :"))
if decision == "Yes":
    print("Good Night!")
else:
    print("Good Evening!")""" 

# *iii. elif:
# examples:
"""day = 6
if day == 0:
    print("Today's SUNDAY")
elif day == 1:
    print("Today's MONDAY")
elif day == 2:
    print("Today's TUESDAY")
elif day == 3:
    print("Today's WEDNESDAY")
elif day == 4:
    print("Today's THURSDAY")
elif day == 5:
    print("Today's FRIDAY")
elif day == 6:
    print("Today's SATURDAY")"""

# * if elif else:
# examples:
"""day = 4
if day == 0:
    print("Today's SUNDAY")
elif day == 1:
    print("Today's MONDAY")
elif day == 2:
    print("Today's TUESDAY")
elif day == 3:
    print("Today's WEDNESDAY")
elif day == 4:
    print("Today's THURSDAY")
elif day == 5:
    print("Today's FRIDAY")
elif day == 6:
    print("Today's SATURDAY")
else:
    print("Please enter valid day.")"""

"""temp = int(input("enter temp : "))
if temp >= 1 and temp <= 10:
    print("Too Cold!!")
elif temp >= 11 and temp <= 20:
    print("Cold!")
elif temp >= 21 and temp <= 30:
    print("Normal Temp!")
elif temp >= 31 and temp <= 40:
    print("Hot!!")
elif temp >= 41 and temp <= 55:
    print("Too HOT with HEAT Waves")
else:
    print("Outoff range!")"""

# *v. nested if elif else:
# Normal time
"""time = int(input("Enter Time (0-12) : "))
zone = input("Enter Time Zone (am / pm) : ")

if zone == "am":
    if time >= 0 and time < 12:
        print("Good Morning, Have a Great Day!")
    else:
        print("wrong input")
elif zone == "pm":
    if (time == 12) or (time >= 1 and time <= 4):
        print("Good Afternoon Sir!!")
    elif time > 4 and time <= 8:
        print("Good Evening Sir!!")
    elif time > 8 and time < 12:
        ask = input("Kya aap sone ja rahe hain (yes / no) : ")
        if ask == "no":
            print("Good Evening Sir!!")
        elif ask == "yes":
            print("Good Night, Sweet Dreams")
        else:
            print("wrong ask input")
    else:
        print("wrong time input")
else:
    print("wrong zone input")"""     

# Float time input
""" time = float(input("Enter Time (0-12) : "))
zone = input("Enter Time Zone (am / pm) : ")

if zone == "am":
    if time >= 0 and time < 11.59:
        print("Good Morning, Have a Great Day!")
    else:
        print("wrong input")
elif zone == "pm":
    if (time >= 12) or (time >= 1 and time < 3.59):
        print("Good Afternoon Sir!!")
    elif time >= 4 and time < 8.59:
        print("Good Evening Sir!!")
    elif time >= 8 and time < 11.59:
        ask = input("Kya aap sone ja rahe hain (yes / no) : ")
        if ask == "no":
            print("Good Evening Sir!!")
        elif ask == "yes":
            print("Good Night, Sweet Dreams")
        else:
            print("wrong ask input")
    else:
        print("wrong time input")
else:
    print("wrong zone input") """

#calculator
"""num_1 = int(input("enter first number : " ))
opr = (input("enter operator : +, -, *, /, %, **, // : ")) 
num_2 = int(input("enter second number : "))

if opr == '+':
    print(num_1 + num_2)
elif opr == '-':
    print(num_1 - num_2)
elif  opr == '*':
    print(num_1 * num_2) 
elif  opr == '/':
    print(num_1 / num_2) 
elif  opr == '%':
    print(num_1 % num_2) 
elif  opr == '**':
    print(num_1 ** num_2) 
elif  opr == '//':
    print(num_1 // num_2)"""

# ?2. Looping Statement :--------------------------------
# *i. while loop:- "entry control loop".
#NOTE: variable_declaration + variable_assignment = variable initialization 
count = 1
while count <= 5:
    print(count)
    count+=1

"""tbl = 2
while tbl <= 20:
    print(tbl)
    tbl+=2""" 

# *ii. for loop:- 
"""fruits = ['apple', 'mango', 'grapes', 'papaya', 'pineapple']
for fruit in fruits:
    print(fruit)"""  

"""sen = "Hello Shree!"
for letter in sen:
    print(letter)"""

"""number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in number:
    if num%2 != 0:
        print("odd : ", num)""" 

"""for num in number:
    if num%2 == 0:
        print("even : ", num)"""

# *iii. break:-
"""for i in range(1, 10):
    if i == 5:
        break
    print(i)"""
    
""" for i in range(5):
    print(i) """

"""alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for char in alpha:
    if char == 'e':
        break
    print(char)"""

# *iv. continue:-
"""for i in range(1, 10):
    if i == 5:
        continue
    print(i)""" 

"""alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for alp in alpha:
    if alp == 'e':
        continue
    print(alp)"""

#! More Examples:-
"""late_time_min = int(input("enter time : "))
inform = input("inform (yes/no) : ")

if inform == "yes":
    if late_time_min >= 15 and late_time_min <= 29:
        print("bhai 50 rupee nikal do.")
    elif late_time_min >= 30 and late_time_min <= 44:
        print("aisa hai chup chap 100 rupee nikal do.")
    elif late_time_min >= 45 and late_time_min <= 59:
        print("beta tum to 150 rupee nikalo.")
    elif late_time_min >= 60 and late_time_min <= 74:
        print("munna, tum ghar ko nikal lo.")
    elif late_time_min >= 75:
        print("kal parents ko lekar aana, abhi nikal jao meri aankon ke samne se!")
    else:
        print("abbe itna late kon aata hai, tu padhna band kar de.")
elif inform == "no":
    print("koi baat nahi, aap ko aaj inform kar diya hai, ab se time par aana.")
else:
    print("bhai sahi se to input dal lo...")"""

# this is mine i add one line 
"""late_time_min = int(input("enter time : "))
inform = input("inform (yes/no) : ")

if inform == "yes":
    if late_time_min >= 1 and late_time_min <= 14:
        print("tum ache bache ho")
    elif late_time_min >= 15 and late_time_min <= 29:
        print("bhai 50 rupee nikal do.")
    elif late_time_min >= 30 and late_time_min <= 44:
        print("aisa hai chup chap 100 rupee nikal do.")
    elif late_time_min >= 45 and late_time_min <= 59:
        print("beta tum to 150 rupee nikalo.")
    elif late_time_min >= 60 and late_time_min <= 74:
        print("munna, tum ghar ko nikal lo.")
    elif late_time_min >= 75:
        print("kal parents ko lekar aana, abhi nikal jao meri aankon ke samne se!")
    else:
        print("abbe itna late kon aata hai, tu padhna band kar de.")
elif inform == "no":
    print("koi baat nahi, aap ko aaj inform kar diya hai, ab se time par aana.")
else:
    print("bhai sahi se to input dal lo...")"""


#* syntax of the nested if:
'''
    variable initialization
    if "condition":
        if "condition":
            -nested if true expression-
        else:
            -nested else false expression-
    elif "more condition":
        if "condition":
            -nested if true expression-
        else:
            -nested if false expression-
    else:
        -false expression-
'''
