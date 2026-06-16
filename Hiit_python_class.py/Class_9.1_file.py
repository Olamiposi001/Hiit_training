file = open("note.txt","r+")
content = file.read()
print(content)
file.seek(7) # move the file pointer to the 7th position and write the new content
file.write("70")
content = file.read()
print(content)
file.close