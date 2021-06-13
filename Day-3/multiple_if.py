# nested if else
print("Welcome to the rollerblade")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("Enjoy your ride")
    age = int(input("What is your age\n"))
    if age <= 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 18
        print("Please pay $18")
    photo = input("Do you want a photo? Y or N\n")
    if photo == "Y":
        bill += 3
    print(f"Final bill {bill}")
else:
    print("Sorry, minimum height for the ride is 120 cm")
