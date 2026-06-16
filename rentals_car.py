rental_car = input("what type of rental car would you like: ")

print(f"let me see if I can find you a {rental_car}.")

#resturant dinning

no_ppl = int(input("How many people are in your dinning group: "))

if no_ppl > 8:
    print("you will have to wait for a table")
else:
    print("Your table is ready")
    
#multiple of ten

Number = int(input("Enter a number: "))

if Number % 10 == 0:
    print(f"The number {Number} is a multiple of ten")
else:
    print(f"The number {Number} is not a multiple of ten")