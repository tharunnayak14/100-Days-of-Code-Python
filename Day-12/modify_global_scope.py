# enemies = 1
#
#
# def increase_enemies():
#     # local scope but we use global enemies to tell there exists another variable
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# # global scope
# print(f"enemies outside function: {enemies}")

enemies = 1


def increase_enemies():
    # local scope but we use global enemies to tell there exists another variable
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
# global scope
print(f"enemies outside function: {enemies}")
