print("Welcome to tip-calculator.")
bill = float(input("What was the total bill?\n"))
percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

bill_and_tip = bill * (100+percentage)/100
each_person = bill_and_tip/people

final_amount = "{:.2f}".format(round(each_person, 2))
# print(type(final_amount))
print(f"Each person should pay: \n{final_amount}")

