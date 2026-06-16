# A Function is a usable block of code that performs a specific task. 
# Functions are reusable, they can be called multiple times in a program.

"""
# Without fuctions
print("Hello, Favour")
print("Hello, Sandra")
print("Hello, Ade")
print("Hello, Chinedu")


# With functions
def greet(name):
    print(f"Hello, {name}")

greet("Favour")
greet("Sandra")
greet("Ade")
greet("Chinedu")
"""

def greet():
    print(f"Hello, Everyone")

# To run the code, call the fuction
greet()
greet()
greet()
greet()
greet()

# Fuctions parameter
# parameter allows functions to receive data from the user


def greet(name):
    print(f"Hello, {name}")

greet("Favour")
greet("Sandra")
greet("Ade")
greet("Chinedu")


def add(a, b, c):
    print(a + b+ c)
    
add(5, 7, 3)


# return values
def add(a, b):
    return a / b


result = add(12, 4)
print(result)

"""
Parameters vs Arguments

arguements are the data pass into a parameter
"""


# Default Parameters


def greet(name="Anonymous User"):
    print(f"Hello, {name}")
    
greet() # Output: Hello, Anonymous User
greet("David") # Output: Hello, David


# Keyword Arguements

def company(name, branch):
    print(name, branch)
    
    
company(branch="Ikeja", name="HiiT")


# Variable Scope: Local Variables

# Local variable is a variable defined in the function

def local_greet():
    name = "favour"
    print(f"Hello, {name}")

local_greet()
    
# Variable Scope: Global Variable

name = "Samuel"

def global_greet():
    print(f"Hello, {name}")
    
global_greet()