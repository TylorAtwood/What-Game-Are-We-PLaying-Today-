#What Game Shall We Play Today???
#This is a randomizer for the listed games I have downloaded (or not downloaded, that be another time?)
#I want this to be my first little project so I can beat COVID-19 boredom
#Tylor Atwood 3/24/20

import random 
import time

#List the games that are fun and playable for me and/or my friends want to play today
games = ["Borderlands 3", "Call of Duty", "Rocket League", "Rainbow 6", "Left for Dead 2", "Minecraft", "Assassin's Creed", "Civ VI"]

#Output to user inroducing the code and what it's about (main interface)

print("W"*120)
print("\t\t\tHello User! Welcome to What Game Shall We Play Today?\n\t\t\t\tEnter 'YES to randomizd game list\t\t\t\t\t\t\t\t\t\tEnter 'q' to quit the program")
print()
print("W"*120)

#The option which correlates with the answer the user selected
proceed = "YES" or "Y" or "Yes" or "yes" or "YEs" or "YeS" or "yES" or "yeS" or "y"
quit = "q"

#Enter YES/ADD/q to proceed
answer = str(input("\t\t\t\t\t"))

#The if/else statement if the user decided to choose the proceed options. If the input is not a option than end program. (Or go back to initial interface)

#If the user chooses to take a chance on the randomizer
if answer==proceed:
   print("Excellent! This may take a minute")
   time.sleep(2.635)
   print(random.choice(games))

#if the user decides to quit the program
if answer==quit:
   print("Thank You and Have a Nice Day!!")
