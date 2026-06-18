# Methods
# methods are functions inside classes or behaviour that can have
class Car:
    color = "Red"
    brand = "Lexus"
    max_speed = "200km/h"
    
    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
        
    def print_properties(self):
        print(f"Color: {self.color}")
        print(f"Brand: {self.brand}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Year: {self.year}")
        
    def get_color(self):
        print(f"Color: {self.color}")

my_car1 = Car(color="Red", brand="Lexus", max_speed="200km/h", year=2020)
my_car2 = Car(color="Blue", brand="Toyota", max_speed="180km/h", year=2019)

print("")
my_car1.print_properties()
print("-------------")
my_car2.print_properties()
print("-------------")
my_car1.get_color()
print("-------------")
my_car2.get_color()