class Animal:
    def __init__(self, name, no_of_legs, sex, color, kingdom):
        self.name = name
        self.no_of_legs = no_of_legs
        self.sex = sex
        self.color = color
        self.kingdom = kingdom
        
       
    def run(self):
        print(f"{self.name} is running.............") 
        
animal_1 = Animal(name="Goat", no_of_legs=4, sex="male", color="white", kingdom="mammal")
animal_2 = Animal(name="Dog", no_of_legs=4, sex="female" , color="black", kingdom="mammal")
    

animal_1.run()
animal_2.run()