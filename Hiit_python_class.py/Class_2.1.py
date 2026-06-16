#List
fruits = ["apple", "banana", "orange"]
#print("Fruits:", fruits)
#find the item based on position(idex)

item = fruits[2] #Read
print(item)
#modifying Editing
fruits[2] = "mango"
print(fruits) #update

#add new item to list
fruits.append("carrot")
fruits.insert(3, "melon")
print(fruits)#update


fruits.remove("carrot")
print("updated Fruits:", fruits)

fruits.pop(3)
print("updated fruits:", fruits)