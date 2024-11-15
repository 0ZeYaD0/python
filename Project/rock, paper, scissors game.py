import random
import os

os.system("cls")

options = ("rock", "paper", "scissors")
player_choice = None
computer_choice = None
if_player_wins = "The player wins"

stop = True
while stop:
    computer_choice = random.choice(options)
    while player_choice not in options:
        player_choice = input("Enter a choice (rock, paper, scissors):\n").lower()
        print(f"You picked: {player_choice}")
        print(f"The computer picked: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie")
        elif player_choice == "rock" and computer_choice == "scissors":
            print(if_player_wins)
        elif player_choice == "paper" and computer_choice == "rock":
            print(if_player_wins)
        elif player_choice == "scissors" and computer_choice == "paper":
            print(if_player_wins)
        else:
            print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no):\n").lower()
    if play_again != "yes":
        stop = False
    player_choice = None

print("Thanks for playing")
