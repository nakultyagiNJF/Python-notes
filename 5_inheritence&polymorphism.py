# Inheritance :-

# Parent Class:----
class Parent:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def data(self):
        print(f"name : {self.name}\n"
              f"city : {self.city}")

# Create Second Class Using Parent Class Inheritance:----
class Child(Parent):
    def __init__(self, name, city, gender, skill):
        Parent.__init__(self, name, city)

        self.gender = gender
        self.skill = skill

    def data(self):
        print(f"name - {self.name}\n"
              f"city - {self.city}\n"
              f"gender - {self.gender}\n"
              f"skill - {self.skill}")


child = Child("Mohan Mishra", "Agra", "Male", "React-JS")
child.data()

mansi = Parent("Mansi Gupta", "Noida")
mansi.data()


"""
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"name is {self.name} and age is {self.age}.")

class Child(Parent):
    def __init__(self, name, age, gender, address):
        Parent.__init__(self, name, age)

        self.gender = gender
        self.address = address

    def data(self):
        print(f"name is {self.name} and age is {self.age}. Gender is {self.gender}. Address is {self.address}.")

child_user = Child("Ayushi Jain", 34, "Female", "Delhi")
child_user.data()
child_user.info()
"""
# Create a class Animal with a method speak().
# Derive a class Dog from Animal that overrides the method speak() to print "Bark".
# Create an object of both and call their methods.

class Animal:
    
    def Voice(self):
        print("Animal Sound")

class Dog(Animal):
    def Voice(self):
        print("Bark")
        
class Elephant(Animal):
    def Voice(self):
        print("Trumpet")

Sound = Animal()
Sound.Voice()

Animal_1 = Dog()
Animal_1.Voice()

Animal_2 = Elephant()
Animal_2.Voice()

# Polymorphism :--
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(10, 20))
print(calc.add(40, 67, 32))