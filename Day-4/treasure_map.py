row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

units = int(position[1])-1
tens = int(position[0])-1

map[units][tens] = 'X  '

print(f"{row1}\n{row2}\n{row3}")