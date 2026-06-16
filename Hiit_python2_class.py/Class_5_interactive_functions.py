""" 
USE OF FUCTIONS IN PYTHON
Write a program that accepts inputs from the user and performs arithmetic operations
using functions:
1.) Create seperate functions that: add, multiply, and divide numbers passed to them
as parameters and return the result
2.)Collect two numbers from the user
3.)use the functions to perform the computation
4.)Display the result of the operation
"""


def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

a = float(input("Enter a number: "))
b = float(input("Enter a second number: "))

# To round the result to 2 decimal places, we can use the format specifier :.2f in the print statement.

add_result = addition(a, b)
print(f"The sum of {a} and {b} is: {add_result: .2f}")

mul_result = multiplication(a, b)
print(f"The product of {a} and {b} is: {mul_result: .2f}")

div_result = division(a, b)
print(f"The quotient of {a} and {b} is: {div_result: .2f}")


try:
    x = float(a)
    y = float(b)
    
    sum_result = addition(x, y)
    # To round the result to 2 decimal places, we can use the round() function.
    rounded = round(sum_result, 2)
    
    
    print(f"The sum is: {addition(x, y)}")
    print(f"The product is: {multiplication(x, y)}")
    try:
        print(f"The quotient is: {division(x, y)}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
    
# print(f"The Difference is: {abs(subtraction(x, y))}")
# abs is a built-in function that returns the absolute value of a number, which is the non-negative value of the number.
