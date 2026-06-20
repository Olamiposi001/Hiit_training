class Person:
    
        
    def __init__(self, f_name, l_name, age):
        self.l = l_name 
        self.f = f_name
        self.age = age
        
    def get_category(self):
        if self.age < 18:
            return "Underage"
        else:
            return "Adult"
        
    def display_details(self):
        print(f"Full Name: {self.l} {self.f}, Age: {self.age}, Category: {self.get_category()}")
        
    def get_age(self):
        print(f"Age: {self.age}")
        
persons = []
no_of_people = 5
for i in range(no_of_people):
        print(f"-----Person {i+1}-----")
        l_name = input("Enter your last name: ")
        f_name = input("Enter your first name: ")
        age = int(input("Enter your age: "))
        person = Person(f_name, l_name, age)
        persons.append(person)
        
for person in persons:
        print("------------------")
        person.display_details()