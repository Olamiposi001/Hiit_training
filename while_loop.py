pizza_toppings = "Enter a pizza topping you like to add too your pizza: "
pizza_toppings += "\nwhen you are done enter quit: "
pizza = ""

active = True
while active:
    pizza = input(pizza_toppings)
    if pizza == "quit":
        active = False
    else:
        print(f"The topping {pizza} will be added to your pizza")