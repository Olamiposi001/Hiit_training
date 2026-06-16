# note = open("note.txt")
# content = note.read()
# note.close()
# print|(content)


import os


def create_file():
    """Createa new file"""
    if os.path.exists(FILE_NAME):
        print(f"{FILE_NAME} already exists")
    else:
        with open(FILE_NAME, "w") as file:
            file.write("Text content for the new file")
            print(f"{FILE_NAME} created successfully")
            
            
            
            
            
# "w", "r", "a", "r+"
FILE_NAME = "student.txt"


note = open("note.txt", "a")
note.write("Hi you are welcome to python class, We are treating file operation")
note.close()

note = open("note.txt", "r")
content = note.read()
note.close()
# print(content)



def write_file():
    """Add data to file without deleting old content"""