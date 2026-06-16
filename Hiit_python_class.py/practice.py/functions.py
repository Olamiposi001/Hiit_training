# def display_message():
#     print("everyone i am learning python in chapter 8")
# display_message()


# def favourite_book(Title):
#     print(f"one of my favourite book is {Title}")
# favourite_book("python_crash_course")

# def make_shirt(size, text):
#     print(f"The shirt is size {size} and the text written on the shirt is \"{text}\"")
# make_shirt(4, "live it love it")
# make_shirt(text="lets go", size=5)


# def make_album(artist_name, album_title, songs=None):
#     album = {"Artist" : artist_name,
#              "Album" : album_title,}
    
#     if songs is not None:
#         album["songs"] = songs
#     return album
        
# Album1 = make_album("Davido", "unavailable")
# Album2 = make_album("Shallipopi", "Ewo", 42)
# Album3 = make_album("919", "123")

# print(Album1)
# print(Album2)
# print(Album3)

def make_album(artist_name, album_title, songs=None):
    album = {"Artist" : artist_name,
             "Album" : album_title,}
    
    if songs is not None:
        album["songs"] = songs
    return album

while True:
    print("Enter Album Information, and enter q to quit")
    
    Artist = input("Enter artist name: ")
    if Artist == q:
        break
    
    Album = input("Enter 
    if A