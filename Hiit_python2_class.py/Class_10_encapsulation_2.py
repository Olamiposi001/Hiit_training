class Car:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        
    def get_Name(
        self,
    ):
        return self.__name
        
        
my_car = Car("Benz", "Red")

print(f"Name: {my_car.get_Name()}")