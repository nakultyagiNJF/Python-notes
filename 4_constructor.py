""" # Constructor Function :-

class Person:
    def __init__(self, name, age, address, skill):
        self.name = name
        self.age = age
        self.address = address
        self.skill = skill
        
    def user_vars(self):
        print(f"name : {self.name}\n"
              f"age : {self.age}\n"
              f"address : {self.address}\n"
              f"skill : {self.skill}")


one_user = Person("Ayushi Jain", 28, "Noida Sec-62", "React-JS")
one_user.user_vars()

second_user = Person("Gopal Verma", 38, "New Delhi", "Back-End")
second_user.user_vars()

third_user = Person("Nakul Sharma", 25, "Gurgaon", "Front-End")
third_user.user_vars() """

# Write a Python class Rectangle that:
# Takes length and width as input in the constructor.
# Has a method area() to return the area of the rectangle.
# Create an object and calculate its area.


class Rectangle:
    def __init__(self, Length, Width):
        self.Lngt = Length
        self.wdth = Width
    
    def area(self):
        return self.Lngt * self.wdth

Area_1 = Rectangle(18, 5)
print(f"Area of the rectangle is : {Area_1.area()}")
Area_2 = Rectangle(12, 4)
print(f"Area of the rectangle is : {Area_2.area()}")