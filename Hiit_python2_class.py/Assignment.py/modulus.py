# create a python file and name it "modulus.py" 
# write a program a number decides if the number is an even or odd number

Num = int(input("Enter a whole number and I will tell you if it's an even or an odd number: "))

if Num % 2 == 0:
    print(f"The number {Num} is an Even Number")
else:
    print(f"The number {Num} is an odd Number")