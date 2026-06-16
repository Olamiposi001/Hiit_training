rental_cars = input("what type of rental car would you like: ")

print(f"\nLet me see if i can find u a {rental_cars}")


restaurant_seatings = input("How many people are in your dinning group: ")
restaurant_seatings = int(restaurant_seatings)
if restaurant_seatings > 8:
    print("you will have to wait for a table")
else:
    print("your table is ready")

number = input("enter a number: ")
number = int(number)

multiple_of_ten = [1, 2, 5, 10]
for multiple in multiple_of_ten:
    if number == multiple:
        print(f"The number {number} is a multiple of ten")
    else:
        print(f"The number {number} is not a multiple of ten")