# rock paper scissors game

import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

figures = [rock, paper, scissors]

your_choice = int(input("What do you want to choose? 1 for Rock, 2 for Paper, 3 for Scissors"))

if your_choice > 3 or your_choice < 1:
    print("Invalid choice You Lose!")
else:

    print(figures[your_choice - 1])
    computer_choice = random.randint(1, 3)
    print("Computer choose:")
    print(figures[computer_choice - 1])

    if your_choice == 1:
        if computer_choice == 2:
            print("You Lose")
        elif computer_choice == 1:
            print("Draw")
        else:
            print("You win")
    elif your_choice == 2:
        if computer_choice == 3:
            print("You Lose")
        elif computer_choice == 2:
            print("Draw")
        else:
            print("You win")
    else:
        if computer_choice == 1:
            print("You Lose")
        elif computer_choice == 3:
            print("Draw")
        else:
            print("You win")
