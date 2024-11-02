import random
import os

os.system("cls")

lowest_number =  1
highest_number = 100

answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Welcome to number guessing game")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:

    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print(f"The number {guess} is out of range")
        elif guess < answer:
            print(f"The number {guess} is less than the answer")
        elif guess > answer:
            print(f"The number {guess} is bigger than the answer")
        else:
            print(f"Correct the answer is {answer}")
            print(f"Your guesses is {guesses}")
            is_running = False
    else:
        print("Invalid input")
        print(f"Please select a number between {lowest_number} and {highest_number}")
    