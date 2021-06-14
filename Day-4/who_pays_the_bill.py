import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


# print(names[random.randint(0, len(names)-1)] + " pays the bill today")
# simply we can use random.choice() directly on a list

print(random.choice(names) + " pays the bill today")