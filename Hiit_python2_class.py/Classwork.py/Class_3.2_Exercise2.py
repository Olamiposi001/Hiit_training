
# write a python that intialize an empty dictionary with the variable name "person" i.e person = {}
# collects personal info from the user: 
# E.g Name, Age, Weight e.t.c and appends it to thr initialized dictionary
# 1.) print the dictionary
# 2.) print all the details the user gave from the dictionary e.g
# Your Name is: Samuel
# Your Age is: 13



person ={}

person["Name"] = input("Enter your name: ")
print(person)

person["Age"] = input("Enter your age: ")
print(person)

person["Height"] = input("Enter your height: ")
print(person)

person["Weight"] = input("Enter your weight: ")
print(person)

print(f"Your Name is {person["Name"]}")
print(f"Your Age is {person["Age"]}")
print(f"Your Height is {person["Height"]}")
print(f"Your Weight is {person.get("Weight")}")