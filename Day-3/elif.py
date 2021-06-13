# nested if else
print("Welcome to the rollerblade")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("Enjoy your ride")
    age = int(input("What is your age\n"))
    if age<=12:
        print("Please pay $5")
    elif age<=18:
        print("Please pay $7")
    else:
        print("Please pay $18")
else:
    print("Sorry, minimum height for the ride is 120 cm")