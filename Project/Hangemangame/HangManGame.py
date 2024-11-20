import random
import os
from Wordlist import words

os.system("cls")


#The art of the hang man is a dictionary of (Key:Values)
hang_man_art = {
            0:("   ",
               "   ",
               "   ",),
            1:(" o ",
               "   ",
               "   ",),
            2:(" o ",
               " | ",
               "   ",),
            3:(" o ",
               "/| ",
               "   ",),
            4:(" o ",
               "/|\\",
               "   ",),
            5:(" o ",
               "/|\\",
               "/  ",),
            6:(" o ",
               "/|\\",
               "/ \\",)
            }

#function to print the art of the hangman
def DisplayMan(wrong_guess):
    print("***************")
    for line in hang_man_art[wrong_guess]:
        print(line)
    print("***************")

#function to print if the player guessed the answer write and replace the _ to the letter
def DisplayHint(hint):
    print(" ".join(hint))
    
#function to display the write answer
def DisplayAnswer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        DisplayMan(wrong_guesses)
        DisplayHint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a valid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            DisplayMan(wrong_guesses)
            DisplayAnswer(answer)
            print("You win!")
            play = input("Do you want to play again (y/n):").lower()
            if play == "y":
                main()
            elif play == "n":
                is_running = False
            
        elif wrong_guesses >= len(hang_man_art) - 1:
            DisplayMan(wrong_guesses)
            DisplayAnswer(answer)
            print("You lose!")
            play = input("Do you want to play again (y/n):").lower()
            if play == "y":
                main()
            elif play == "n":
                is_running = False

if __name__ == "__main__":
    main()