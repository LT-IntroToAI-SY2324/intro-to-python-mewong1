# We will write a rock paper scissors game in class - Complete it in this file
import random



player_choice = "rock"
computer_choice = "paper"

def get_choices():
    player_choice = input("Enter rock, paper or scissors")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    if player_choice == computer_choice:
        return "You tied!"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "You lost!"
        elif computer_choice == "scissors":
            return "You won!"
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "You won!"
        elif computer_choice == "scissors":
            return "You lost!"
     elif player_choice == "scissors":
        if computer_choice == "rock":
            return "You lost!"
        elif computer_choice == "paper":
            return "You won!"
    # return player_choice
    return choices

choices = get_choices()

print(choices)