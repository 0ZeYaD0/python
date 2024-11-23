import requests

base_url = "https://random-word-api.herokuapp.com/word?lang=en"
response = requests.get(base_url)

if response.status_code == 200:
    word = response.json()[0]
else:
    print("Failed to fetch words from the API.")
    word = "default"

# The art of the hangman is a dictionary of (Key:Values)
hang_man_art = {
    0: ("   ",
        "   ",
        "   ",),
    1: (" o ",
        "   ",
        "   ",),
    2: (" o ",
        " | ",
        "   ",),
    3: (" o ",
        "/| ",
        "   ",),
    4: (" o ",
        "/|\\",
        "   ",),
    5: (" o ",
        "/|\\",
        "/  ",),
    6: (" o ",
        "/|\\",
        "/ \\",)
}

# Function to print the art of the hangman
def DisplayMan(wrong_guess):
    print("***************")
    for line in hang_man_art[wrong_guess]:
        print(line)
    print("***************")

# Function to print the current hint
def DisplayHint(hint):
    print(" ".join(hint))

# Function to display the correct answer
def DisplayAnswer(answer):
    print(" ".join(answer))

def main():
    answer = list(word)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while wrong_guesses < 6 and "_" in hint:
        DisplayMan(wrong_guesses)
        DisplayHint(hint)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

    if "_" not in hint:
        print("Congratulations! You guessed the word:")
    else:
        print("Game over! The correct word was:")

    DisplayAnswer(answer)

if __name__ == "__main__":
    main()