print(f"\"the\n has\t fallen\"")

whole_number1 = int(input("input a whole number: "))
whole_number2 = int(input("input a second whole number: "))

sum_of_whole_numbers = whole_number1 + whole_number2

print(f"The sum of the whole numbers you enter previously is: {sum_of_whole_numbers}.")
print((3*5), (6**4))

John = 3

Mary = 5

Adam = 6

print(f"{John}, {Mary}, {Adam}")

print(John, Mary, Adam, sep = ",")

print(John + Mary + Adam)

Total_Apples = John + Mary + Adam
print(Total_Apples)

price = float(input("What's the price of tomato:  "))

if price < 1:
    print("that is cheap, buy a lot")
    
elif price < 3:
    print("okay, buy few")
    
else:
    print("too much, buy some carrot instead.")