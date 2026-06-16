newlist = [3, 5, 2, 7, 8, 6, 4, 1]
Item = newlist[-2]
print(Item)

profile = {"name": "Bolu", "age": "25", "city": "Lagos"}
keyValue = profile["age"]
print(keyValue)


newlist[3] = 10
print(newlist)

profile["name"] = "Edward"

print(profile)


newlist.pop(3)
print(newlist)


profile.pop("age")
print(profile)

newlist.append(13)
print(newlist)