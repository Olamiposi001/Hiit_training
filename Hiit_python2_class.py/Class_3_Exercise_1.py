start = 1
stop = 10
step = 2
for k in range(start, stop +1, step):
    print(k)
    print("hello world")
    
    
# A python program that prints all the multiples of 5 from 1 - 200
# 1, 2, 3, 4, ----- 200
for i in range(1, 201):
    if i % 5 == 0:
        print (i)
        

class_list = ["David", "Samuel", "Gafar", "Rayyan", "Odufua", "favour"]

for person in class_list:
    print(person.title())
    
    
    
# i want to use while to print 1 - 10

number = 1
end = 10
while number < end + 1:
    print (number)
    number = number + 1
    
    
    
#  using while loop to loop through thr list










# Dictionary
# Key - Values pairs

table = {
    "name" : "Table_1",
    "height" : "10cm",
    "width" : "25",
    "color" : "red"
}

print(table["name"])

color = table.get("color")

print(color)

height = table.get("heights")

print(height)


# Appending a Dictionary

table["names"] = class_list

print (table)