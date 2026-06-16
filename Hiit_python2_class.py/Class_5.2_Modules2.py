from Class_5_modules import addition, multiplication, division, subtract

try:
    a = float(input("Enter a Number: "))
    b = float(input("Enter another Number: "))

except ValueError:
    print("Error occured with the Values entered")
    
add_result = addition(a, b)
print(f"The addition of {a} and {b} is {add_result}")

try:
    sub_result = subtract(a, b)
    print(f"The subtraction of {a} and {b} is {abs(sub_result)}")
except ZeroDivisionError:
    print("ERROR: invalid input value")
    
mul_result = multiplication(a, b)
print(f"The multiplication of {a} and {b} is {mul_result}")

Div_result = division(a, b)
print(f"The division of {a} and {b} is {Div_result: .2f}")