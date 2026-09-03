# Operators :-
"""
    defination: OOO (Operator Operates the Operends)
    explaination: O - Operators like as +,-,*,/,%, etc.
                  O - Operates/Operation like as a+b, a-b, a*b, etc.
                  O - Operands/Values like as 1, 2, 56, 78, etc.
"""

''' There are 7 different types of operator in Python:
    1. Arithmetic Operators
    2. Assignment Operators 
    3. Comparison Operators
    4. Logical Operators
    5. Identity Operators
    6. Membership Operators
    7. Bitwise Operators
'''
  
"""1. Arithmetic Operators :- 
    Addition(+), Subtraction(-), Multiplication(*), Division(/), Modules(%), Power(**), FloorDivision(//) """ 
# examples:-
a = 90
b = 78.5
print(a + b)

a = 56
b = 89
print(a - b)

a = 12
b = 8
print(a*b)

a = 556
b = 6
print(a/b)

a = 28
b = 16
print(a%b)

a = 2
b = 4
print(a**b)

a = 78
b = 48
print(a//b)

# print("10" + 10)
# string or number ka addition nahi ho sakta hai, ya to string string ka concatination hoga ya, number number ka addition hoga.
print("90" + "89")
print("Tushar" + "Sharma")

# print("5" + 4 + 3 + 2 + 1)
# print(1 + 2 + 3 + 4 + "5")


"""2. Assignment Operators :-
    Equal(=), PluseEqual(+=), MinusEqual(-=), MultipyEqual(*=), DivideEqual(/=), ModuleEqual(%=), FloorDivisionEqaul(//=), PowerEqual(**=)"""
# examples:
a = 90
a+=89 # a = a + 89
print(a)

a = 90
a-=67
print(a)

a = 45
a*=5
print(a)

a = 45
a/=5
print(a)

a = 87
a%=65
print(a)

a = 76
a//=45
print(a)

a = 13
a**=2
print(a)

"""3. Comparison Operators :-
    DoubleEqual(==), NotEqual(!=), GreaterThan(>), LessThan(<), GreaterThanAndEqualTo(>=), LessThanAndEqualTo(<=)"""
# examples:
a = 90
b = 97

print(a == b)

print(a != b)

print(a > b)

print(a < b)

print(a >= b)

print(a <= b)

"""4. Logical Operators :-
    (and), (or), (not)"""
'''basically Logical  Operators more than 1 conditions lagane ke liye use kiye jate hain.'''
'''
0 - false
1 - true
    (i). and == 'and' operator bilkul multiplication ke trah kaam karta hai. jaise 0*0=0, 0*1=0, 1*0=0, 1*1=1
    0 0 - 0
    0 1 - 0
    1 0 - 0
    1 1 - 1
    note: isme aap ki sari conditions true honi chahiye tabhi aap ko result true milega.

    (ii). or == 'or' operator bilkul addition ki trah hi kaam karta hai. jaise 0+0=0, 0+1=1, 1+0=1, 1+1=1
    0 0 - 0
    0 1 - 1
    1 0 - 1
    1 1 - 1
    note: isme agar dono hi condition false hain, to hi aap ko result false milega.

    (iii). not == jaise 0=1, 1=0
    0 - 1
    1 - 0
    note: ye operator bilkul invert kaam karta hai, means true ko false or false ko true kar deta hai. 
'''
# examples:
# ---and----
a = 56
b = 45
print((a > b) and (a == b)) # 1 and 0 => 0(False)
print((a > b) and (b < a)) # 1 and 1 => 1(True)

# ---or---
age = 18
print((age > 18) or (age < 20)) # 0 or 1 => 1(True)
print((age > 18) or (age < 15)) # 0 or 0 => 0(False)

# ---not---
count = 8
print(not(count > 5)) # not(1) => 0(False)
print(not(count > 56)) # not(0) => 1(True)

"""5. Identity Operators :-
    (is), (is not)"""
# examples: 

age = 23
print(age is 23)

name = "Tushar Sharma"
print(name is 'Tushar Sharma')

print(age is not 23)
print(name is not "Mohan Sharma")

"""6. Membership Operators :-
    (in), (not in)"""
# examples:
sen = "I love Python Programming Language."
print("love" in sen) # True
print("." in sen) # True
print('i ' in sen) # False
print('i ' not in sen) #True
# note: membership operators case-sensitive hote hain, means letter small or capital is not equal.

"""7. Bitwise Operators :-
    AND(&), OR(|), XOR(^), NOT(~), ZeroFillLeftShift(<<), SignedRightShift(>>)"""
# examples:
# First take these value if there is big number you can go 2 ke multiple      8 4 2 1
#                                                                         9 - 1 0 0 1
#                                                                         5 - 0 1 0 1
#                                                                         -----------
# And(&) value will be multiple                                           & = 0 0 0 1
# OR(|) value will be add                                                 | = 1 1 0 1
# XOR(^) if there is same value there will(0) if different there will(1)  ^ = 1 1 0 0
a = 9
b = 5
print(bin(a))
print(bin(b))
print(bin(a & b))
print(bin(a << b))
print(bin(a >> b))
print(bin(~a))
print(bin(~b))
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)
print(~a)
print(~b)

'''here, "bin()" function ka use kisi bhi decimal number ko binary me convert krne ke liye kiya jata hai.
note: bitwise operater binary par hi kaam karte hain.'''

#! 2 digit bitwise 

#        64 32 16 8 4 2 1
# 67 =   1  0  0  0 0 1 1
# 45 =   0  1  0  1 1 0 1
# & =    0  0  0  0 0 0 1
# | =    1  1  0  1 1 1 1

a = 67
b = 45
print(bin(a))
print(bin(b))
print(bin(a & b))
print(bin(a ^ b))
print(bin(a << b))
print(bin(a >> b))
print(bin(~a))
print(bin(~b))
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)
print(~a)
print(~b)    