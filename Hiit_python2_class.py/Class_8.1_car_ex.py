class Car:
    color = "Red"
    brand = "Lexus"
    max_speed = "200km/h"
    
    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year

my_car1 = Car(color="Red", brand="Lexus", max_speed="200km/h", year=2020)
my_car2 = Car(color="Blue", brand="Toyota", max_speed="180km/h", year=2019)

my_car2.color = "White"
my_car3 = Car(color="Pink", brand="Toyota", max_speed="250km/h", year=2021)

print(my_car1.color)
print(my_car1.brand)
print(my_car1.max_speed)
print(my_car1.year)
print("-----------------")
print(my_car2.color)
print(my_car2.brand)
print(my_car2.max_speed)
print(my_car2.year)
print("-----------------")
print(my_car3.color)
print(my_car3.brand)
print(my_car3.max_speed)
print(my_car3.year)
