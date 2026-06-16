age_prices = "enter your age to get your ticket price: "

age = ""
active = True
while active:
    age = input(age_prices) 
    age = int(age)

    if age < 3:
        print(f"your ticket price is free")
    if age >= 3 and age <= 12:
        print("your ticket fee is $10")
    if age > 12:
        print("your ticket fee is $12")