prompt = "\nI will back anything to you:"
prompt += "\nEnter 'quit' to quit."

kp = True

while kp == True:
    message = input(prompt)
    if message == 'quit':
        kp = False
    else:
        print(message)

print('goodbye.')