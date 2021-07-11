# file = open("my_file")
# content = file.read()
#
# print(content)
#
# file.close()

# automatically closes
# with open("my_file") as file:
#     content = file.read()
#     print(content)

# write to file
# change mode to write

# deletes everything from the file
with open("my_file", mode="w") as file:
    file.write("America")

# use append mode to add to a file
with open("my_file", mode="a") as file:
    file.write("\nAmerica")

# create a new file
with open("new_my_file", mode="w") as file:
    file.write("India")