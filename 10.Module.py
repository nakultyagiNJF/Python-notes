# !Modules :---->
# *Consider a modules to be the same as a code library.
# *A file containing a set of functions you want to include in your application. 

# -----------------------------------------
# import existing file:
import data
# call functions:
data.add(10, 30)
data.info("Mohan Kumar", 29, "kumarmohanER@gmail.com")

# use variables:
name = data.name
print(f"My name is {name}.")

# use dictionary:
skills = data.user["skills"]
print(skills)

# -----------------------------------------
# import existing file:
import data as d

# use dict:
informtion = d.user["age"]
print(informtion)

# -----------------------------------------
# import existing file info function:
from data import info

# using the function:
info("Gopal Verma", 43, "vermaGP@gmail.com")