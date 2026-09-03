#Rules of the Variables :-

"""
    * A variable name must start with a letter or the underscore character. 
    * A variable name cannot start with a number.
    * Variable names are case-sensitive (age, Age and AGE are three different variable)
    * A variable name cannot be any of the Python keyword. 
    * A variable name can only contain alphanumerical characters and underscore (A-z, 0-9, and _ ).
"""

""" There are three ways to create a variable name:
1. camelCase
2. PascalCase
3. snake_case 
"""

#1. camelCase - Second name first letter will be capital 
userName = "Gopal Verma"
firstName = "Ayushi"
lastName = "Sharma"                                                                                           
 
#2. PascalCase - Both name first letter will be capital 
UserName = "Who am I?"
UserEmail = "who886@gmail.com"

#3. snake_case - After every name you will use
user_login_form = "True"

# This code is use to know all the latest keyword of the python and you can't use keyword as first letter/word in variable  

import keyword
print(keyword.kwlist) 