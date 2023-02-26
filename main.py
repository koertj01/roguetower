name = input("Please enter your name: ")
print(f"Hello: {name} ")

while True:
    action = input("Please type EXIT to exit: ")
    if action.upper() == "EXIT": # we want to check for any case for the match
        exit()
    else: 
        print("you are at the main menu")

print("thank you for playing")