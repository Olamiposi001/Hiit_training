class NewBrand:
    def __init__(self):
        self.brand = "pepsi"
        self.author = "peace"
        
        
# Initialization

personBrand = NewBrand()
print(personBrand.brand)

class person:
    # class Attributes
    # laptop = "HP"
    
    def __init__(self, name, brand, food): 
        # instance Attribute
        self.name = name
        self.brand = brand
        self.food = food
        
    def greeting(self):
        print(f"Hello my name is {self.name}, good afternoon")
        
personbrand = person("peace", "pepsi", "name")
print(personbrand.brand)