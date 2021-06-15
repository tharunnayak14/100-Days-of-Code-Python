import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# EASY VERSION
# new_password = ""
#
# for i in range(1, nr_symbols + 1):
#     new_password += random.choice(symbols)
# for i in range(1, nr_numbers + 1):
#     new_password += random.choice(numbers)
# for i in range(1, nr_letters + 1 - (nr_symbols + nr_numbers)):
#     new_password += random.choice(letters)
#
# print(new_password)

# HARD VERSION (random order)
# here we store the chars into a list rather than a string
new_password = []

for i in range(1, nr_symbols + 1):
    new_password.append(random.choice(symbols))
for i in range(1, nr_numbers + 1):
    new_password.append(random.choice(numbers))
for i in range(1, nr_letters + 1 - (nr_symbols + nr_numbers)):
    new_password.append(random.choice(letters))

# use random.shuffle to shuffle the contents of the list, so they are arranged in a random order
random.shuffle(new_password)

# finally create a string for final password from the shuffled list
final_password = ""
for char in new_password:
    final_password += char
print(f"Your password is: {final_password}")