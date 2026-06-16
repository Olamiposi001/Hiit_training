# What is OOP
# A programming paradigm that organizes code into objects, which combibe:

# *Data (attributes)
# *Behaviour(methods)

# Benefits of OOP

# What is a class?
# A class a blueprintnor template used to create an object

# Attributes and Methods

# Attrbutes
# variables belonging to a class

# Methods
# 

# OOP programming

# Example 1
class Animal:
    name = "goat"
    kingdom = "mammal"

animal_1 = Animal()

print(f"Animal name is {animal_1.name} ")
animal_1.name = "cow"

# talking about methods

# init is a method that help us 
class Car():
    
    # usedto initialize the attributes of a class
    def __init__(self, name, brand, no_of_wheels):
        self.name = name
        self.brand = brand
        self.no_of_wheels = no_of_wheels
    
    def accelerate(self):
        print(f"{self.name} is accelerating............")
        
ferrari = Car(name="Favour's Ferrari", brand="Mobile car", no_of_wheels=4)
ferrari_2 = Car(name="Samuel's car", brand="Toyota", no_of_wheels=4)


# inheritance

# EX 1:

class Dog(Animal):
    pass

my_dog = Dog(name="Tig", no_of_legs=4)
print(my_dog.name)

# EX: 2
class Dog(Animal):
    def nameLeg(self):
        print(f"Name: {self.name}")
my_dog = Dog(name="Tig", no_of_legs=4)
print(my_dog.name)
        
