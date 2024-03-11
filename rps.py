# Boring variables and imports
import os
import random
wm = 'made by Vastitude c. 2024 :)'
choice = 'Pick your choice (rock, paper or scissors):'
replay = "Do you want to play again? (y/n):"

# Code to get the computer to actually play
while True:
 rps = ["rock", "paper", "scissors"] # The choices the computer has
 comp_action = random.choice(rps) # Pick an option in comp_rps

# Print choice
 print (choice)

# User input and loop
 user_action = input()
    
# The bread and butter (the logic)
 if user_action == comp_action:
    print (f"Both players chose {user_action}. It's a tie!") # If both computer and player choose the same, it's a tie
 elif user_action == "rock":
     if comp_action == "scissors": # - and computer chose scissors;
         print ("Rock smashes scissors - you win!")
     else:
         print ("Paper covers rock - you lose.")
 elif user_action == "paper": # If user chose paper -
       if comp_action == "rock": # - and computer chose rock;
          print ("Paper covers rock - you win!")  
       else:
        print ("Scissors cut paper - you lose.")
 elif user_action == "scissors": # If user chose scissors -
        if comp_action == "paper": # - and computer chose paper;
            print ("Scissors cut paper - you win!")
        else:
            print ("Rock smashes scissors - you lose.")
            
 print (replay)
 play_again = input()
 if play_again.lower() != "y":
     print (wm)
     break