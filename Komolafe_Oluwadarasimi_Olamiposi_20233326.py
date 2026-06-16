def  diagnose_system():
    print("system diagnose program" )
    print("Let's find out what is wrong with your system")

    screen = input("Is the screen turning on? (yes/no): ").lower()
    if screen == "no":
        print("maybe the screen is broken or isn't connected properly.")
    else:
        print("the screen isn't the problem")

    buttons = input("are the buttons working properly?  (yes/no) " ).lower()
    if buttons == "no":
        print("the buttons might be stuck or broken.")
    else:
        print("the buttons aren't the problems.")
    
    sound = input("is the sound work9ng well. (yes/no) ")
    if sound == "no":
        print("there might be something wrong with the speakers or the sound settings are not well set. (yes/no) ")
    else:
        print("the sound isn't the problem." )

    print("If this is of help to you, you are welcome. ")

    print("But if any of this are not the problem or the problem continues ask an expert for help. ")
diagnose_system()