import random

logo = """
  /$$$$$$                                                 /$$     /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                               | $$    | $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/                                                                                                                                                               
"""
def game():
    print(logo)

    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1-100")
    # asking user for game difficulty
    difficulty = input("choose a difficulty, type 'easy' or 'hard':")

    # a function to pick a random number between 1-100
    def pick_number():
        return random.randint(1, 100)

    # easy: no_of_guesses = 5
    # hard: no_of_guesses = 10
    no_of_guesses = 5
    if difficulty == 'easy':
        no_of_guesses = 10

    # creating a variable to store a random number between 1-100
    picked_number = pick_number()

    while True:
        print(f"You have {no_of_guesses} attempts remaining to guess the number")
        # ask user to make a guess
        guess = int(input("Make a guess:\n"))

        # game logic
        if guess == picked_number:
            print("Yeah, you guessed the number")
            break
        elif guess > picked_number:
            print("Too high")
        else:
            print("Too low")

        # if user fails to guess decrease no_of_guesses
        no_of_guesses -= 1

        # if user has more lives left give him another chance to guess the number
        if no_of_guesses > 0:
            print("Guess again")
        # else game over and print the picked_number
        else:
            print("You ran out of guesses")
            print(f"The number I'm thinking is {picked_number}")
            break

game()

