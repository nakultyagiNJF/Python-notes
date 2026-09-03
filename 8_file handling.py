# !File Handling
# File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.

""" 
    • The key function for working with files in Python is the open() function.
    • The open() function takes two parameters; filename, and mode.
"""
# There are four different methods(modes) for opening a file:
""" 
    • "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    • "a" - Append - Opens a file for appending, creates the file if it does not exist
    • "w" - Write - Opens a file for writing, creates the file if it does not exist
    • "x" - Create - Creates the specified file, returns an error if the file exists 
"""
#   In addition, you can specify if the file should be handled as binary or text mode
""" 
    • "t" - Text - Default value. Text mode
    • "b" - Binary - Binary mode (e.g. images)
"""

# ?Select any file and open it:
# To open a file for reading it is enough to specify the name of the file:

"""f = open("1_Introd.ipynb")
print(f)"""
# <_io.TextIOWrapper name='1_Introd.ipynb' mode='r' encoding='cp1252'>

"""f = open("1_Introd.ipynb", "rt")
print(f)"""

# note: Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# <_io.TextIOWrapper name='1_Introd.ipynb' mode='rt' encoding='cp1252'>

"""f = open("demo.txt", "rt")
print(f)"""
# <_io.TextIOWrapper name='demo.txt' mode='rt' encoding='cp1252'>

# ?Read any file :
"""f = open("1_Introd.ipynb")
r = f.read()
print(r)"""

"""f = open("demo.txt", "rt")
r = f.read()
print(r)"""

# ReadLine :
"""f = open("demo.txt", "rt")
r = f.readline()
print(r)"""

"""r2 = f.readline()
print(r2)"""

# With loop:
"""f = open("demo.txt", "rt")
for i in f.readlines():
print(i)"""

#Closing File :
"""f = open("demo.txt", "rt")
r = f.read()
print(r)
f.close()"""

# note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# ?Write to an Existing File :
# To write to an existing file, you must add a parameter to the open() function:
""" 
    • "a" - Append - will append to the end of the file
    • "w" - Write - will overwrite any existing content
"""

# appending -
"""f = open("demo.txt", "a")
f.write("\nHello Shree, How can i hello you?")
f.close()"""

"""f = open("demo.txt", "rt")
r = f.read()
print(r)
f.close()"""

# writing -
"""f = open("demo.txt", "w")
f.write("Name: Gopal Verma\nAge: 28\nCity: San Francisco")
f.close()"""

"""f = open("demo.txt", "rt")
r = f.read()
print(r)
f.close()"""

"""file = open("text.txt", "w")
file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw")
file.close()"""

# note: jab bhi aap aise file ko write mode me open karte ho jo... existe hi nahi karti hai to vo file create ho jati hai. or fir aap usme data enter kar sakte ho.

"""file = open("random.txt", "a")
file.write("This is the random file.")
file.close()"""

# note: jab bhi aap aise file ko append mode me open karte ho jo...existe hi nahi karti hai to vo file create ho jati hai. or fir aap usme data enter kar sakte ho.

# ?CREATE A NEW FILE USING PYTHON FORMATE :
# To create a new file in Python, use the open() method with one of the following

# parameters:
"""
    • "x" - Create - will create a file, returns an error if the file exist
    • "a" - Append - will create a file if the specified file does not exist
    • "w" - Write - will create a file if the specified file does not exist
"""
"""f = open("text.txt", "x")
f.close()"""
# output: FileExistsError: File exists: 'text.txt'

"""f = open("rough.py", "x")
f.close()"""

"""f = open("rough.py", "a")
f.close()"""

"""f = open("basics.py", "a")
f.close()"""

# ?Delete a File:
# To delete a file, you must import the OS module, and run its os.remove() function:
"""import os
os.remove("basics.py")"""

"""import os
if os.path.exists("rough.py"):
os.remove("rough.py")
else:
print("The file does not exist")"""

# Delete a Folder:
"""import os
os.rmdir("rmdFolder")"""