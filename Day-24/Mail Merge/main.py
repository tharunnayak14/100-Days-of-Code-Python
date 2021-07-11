PLACEHOLDER = "[name]"


# create a list of names to invite
with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

# now copy the contents of the starting letter

with open("Input/Letters/starting_letter.txt") as start_letter:
    contents = start_letter.read()
    for name in names:
        # to remove /n
        name = name.strip()
        # replace the ["name"] with the name of the person
        new_letter = contents.replace(PLACEHOLDER, name)
        # now create new text files with everyone's name on it
        with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)