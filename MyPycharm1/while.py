ff={}

prompt = "\nName&Food"
prompt += "\n'quit'"

kr=True

while kr == True:
    name=input('Name')
    if name != 'quit':
        food=input('Food')
        ff[name]=food
    else:
        kr=False

#print(ff.keys())

for name in sorted(ff.keys()):
    print(name,food)

print('\nGoodbye.')