user_names = ["Admin", "Desola", "Bola", "Darasimi", "Samson"]


for user_name in user_names:
    if user_name == "Admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in today")
        
alien_color = {"green", "red", "blue", "white"}

for color in alien_color:
    if color == "green":
        print("You just earned 5 points for shoot alien")
    else:
        print("You just earned 10 points for shoot alien")
for color in alien_color:        
    if color == "green":
        print("You just earned 5 points for shoot alien")
    if color != "green":
        print("You just earned 10 points for shoot alien")

