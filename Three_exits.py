#version 1 using conditional statement
pizza_with_toppings = "please enter a topping you would like to enter in your pizza: "
pizza_with_toppings += "\nenter quit to stop adding a topping "
topping = ""

while topping != "quit":
    topping = input(pizza_with_toppings)

    if topping != "quit":
        print(f"{topping} topping has been added to your pizza.")


#version 2 using an active variable

pizza_with_toppings = "please enter a topping you would like to enter in your pizza: "
pizza_with_toppings += "\nenter quit to stop adding a topping "
topping = ""

active = True
while active:
    topping = input(pizza_with_toppings)
    if topping == "quit":
        active = False
    else:
        print(f"{topping} topping has been added to your pizza.")

#version 3 using break statement

pizza_with_toppings = "please enter a topping you would like to enter in your pizza: "
pizza_with_toppings += "\nenter quit to stop adding a topping "
topping = ""

while True:
    topping = input(pizza_with_toppings)
    if topping == "quit":
        break
    else:
        print(f"{topping} topping has been added to your pizza.")