import os
file = open("note.txt", "r")
content = file.read()
print(content)
file.seek(0, os.SEEK_END)  # Move the file pointer to the end of the file

file.write("70")  # Write "70" at the end of the file
content = file.read()  # This will not read anything as the file pointer is at the end
print(content)  # This will print an empty string
file.close()  # Close the file
