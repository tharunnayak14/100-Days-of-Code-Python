################### Scope ####################

enemies = 1


def increase_enemies():
    # local scope
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
# global scope
print(f"enemies outside function: {enemies}")

# local scope
# def function():
#     variable = 10
# function()
# print(variable)

# Global scope
health = 10

def kill():
    health = 0

kill()
print(health)
