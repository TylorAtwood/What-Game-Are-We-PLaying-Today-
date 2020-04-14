#!/usr/bin/env python3
#Tylor Atwood
#Hi-Lo Game
#4/14/20

#This is a def to inlcude the guessing game. 
def game():

    #Immport random library 
    import random

    #Declare varibles. Such as max number, generated random number, and user's number guess
    max = int(input("What should the maximum number for this game be?: "))
    print("\n")
    num = random.randint(1,max)
    guess = int(input("Guess my number: "))

    #While loop for guessing number
    while guess != num:
        if guess > num:
            print("Your guess is too high") #Number is higher than generated random number
            print("\n")
            guess = int(input("Guess my number: "))
            
        if guess < num: 
            print("Your guess is too low")#Number is lower than generated random number
            print("\n")
            guess = int(input("Guess my number: "))
            
        if guess == num:
            print("You guessed my number!") #User guess the number right
            print("\n")
            restart = input("Do you wish to play again? (Y/N)") #Asking the user to restart guessing game. This is why I declared the game as a def. 
            if restart == "Y":
                game() #restarts game. Goes back to the top of the program. 
            else: print("Thanks for playing!") #If the user does not want to restart. It ends the program
            exit #Exits program
game()



