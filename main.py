
######
#basic game loop referenced in most TUTS
#init() //This runs once unless we need to regen the whole game
#processInput() //we know what this does
#update() //game logic updates and state changes
#render() //draw it dude
#run() //any update functionality goes here outside of user controls and UI
######

#imports
import components.command.py

#this be the main loop here
print("Welcome to the ultimate game")
while True:
    action = input("Please type EXIT to exit: ")
    if action.upper() == "EXIT": # we want to check for any case for the match
        break #break from the main loop and goto end statement
    else: 
        print("YOU ARE AT THE MAIN MENU")
        continue #do more stuff
        ## we can also use a var to set change status

print("thank you for playing")