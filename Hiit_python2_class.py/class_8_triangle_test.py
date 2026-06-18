class Rectangle:
    color = "red" # Creating an attribute inside the class itself
    def __init__(self, l, b):
        self.lenghth = l
        self.breadth = b
        self.color 
        
obj1 = Rectangle(l=30, b=60)

print(obj1.lenghth, obj1.color)


class Vehicle:
    running = False
    
    def __init__(self, owner):
        self.owner = owner
        
    def is_running(self):
        if self.running:
            print(print(f"{self.owner}'s vehicle car is runing"))
        else:
            print(print(f"{self.owner}'s vehicle car is not running"))
            
v1 = Vehicle(owner= "Olamiposi Darasimi")
print(v1.is_running())