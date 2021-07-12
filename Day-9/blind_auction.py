logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
import os



print("Welcome to the blind auction")

bidders = {}

max_bid = 0
continue_next = True
while continue_next:
    name = input("Enter your name:\n")
    bid = int(input("Please enter your bid:\n"))

    bidders[bid] = name
    max_bid = max(bid, max_bid)

    choice = input("Does anyone else want to bid? yes or no:\n")

    if choice == "yes":
        os.system('cls')
    else:
        continue_next = False

print(f"The winner is {bidders[max_bid]}")
