prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = input(prompt)
while message != 'quit':
    if message != "quit":
        print(message)
