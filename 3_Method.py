"""# Class in Methods :

# example 1:

# create a class-
class Person:
    name = "Tushar Sharma"
    age = 34
    city = "New Delhi"

    # create a method-
    def my_info(self):
        print(f"My name is {self.name}. I am {self.age} years old. I am living in {self.city}.")

# create an object-
user = Person()
user.my_info()


# example 2:
# create a class-
class Person:
    name = "Tushar Sharma"
    age = 34
    city = "New Delhi"

    # create a method-
    def my_info(self, job, skill):
        print(f"My name is {self.name}. I am {self.age} years old. I am living in {self.city}. My skill is {skill}. And Job {job}.")

# create an object-
user = Person()
user.my_info("Yes", "Full-Stack Developer")

# create an object with new data-
new_user = Person()
new_user.name = "Mohan Kumar"
new_user.age = 45
new_user.city = "Gurugram"
new_user.my_info("Yes", "Python Developer")"""

# Q1. Class & Object
# Create a class Student with attributes: name and marks.
# Add a method display() that prints the student’s details.
# Create 2 student objects and call the method.

class Student:
    name = "Vaibhav Sharma"
    marks = 67

    def result(self):
        print(f"My name is {self.name}. I got {self.marks} marks.")

Student1 = Student()
Student1.name = "Vaibhav Sharma"
Student1.marks = 67
Student1.result()

Student2 = Student()
Student2.name = "Aditi Verma"
Student2.marks = 72
Student2.result()
